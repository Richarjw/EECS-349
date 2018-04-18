import numpy as np
from node import Node
from parse import parse
import copy

inFile = "/Users/Nico/Documents/GitHub/EECS-349/HW1/house_votes_84.data"
Data = parse(inFile)  


def count_class(examples,class_name, class_type):
	'''
	counts the numebr of class_types in example space given class_name.
	'''
	count = 0 
	for item in examples:
		if (item[class_name] == class_type):
			count += 1
	return count




def mode(examples):
    unique = {}
    for item in examples:
        if item['Class'] not in unique:
            unique[item['Class']] = 0 #Create dictionary

    for item in examples:
        unique[item['Class']] += 1
	
    return max(unique)




def compute_conditional_prob(examples, attribute_name, attribute_type, class_name):
	'''
		computes probability of given attribute/attribute_type pair given its of a certain class
		name (rep or dem)
	'''
	numerator = 0
	total = 0 
	
	for item in examples:
		total += 1
		if (item[attribute_name] == attribute_type and item['Class'] == class_name):
			numerator += 1
	
	return float(numerator) / float(total)



def entropy(examples,name):

    total_tally = 0
    class_tally = {}
    for item in examples: #Create dictionary of classes
        total_tally+=1
        if item['Class'] not in class_tally:
            class_tally[item['Class']] = 1 
        else:
            class_tally[item['Class']] += 1

    options = {}
    for item in examples:
        if item[name] not in options:
            options[item[name]] = 0

            
    class_labels = {}
    for item in examples: #Create dictionary of classes
        if item['Class'] not in class_labels:
            class_labels[item['Class']] = copy.copy(options)


    for item in examples:
        class_labels[item['Class']][item[name]] +=1

    name_tally = {}
    for item in examples: #Create dictionary of classes
        if item[name] not in name_tally:
            name_tally[item[name]] = 1 
        else:
            name_tally[item[name]] += 1


    probs = []
    for class_label in class_labels:
        for sub_label in class_labels[class_label]:
            p_y_x = float(class_labels[class_label][sub_label])/float(total_tally)
            p_x = float(name_tally[sub_label]) / float(total_tally)
            if p_y_x > 0:
                probs.append(p_y_x*np.log2(p_x/p_y_x))
                
    return sum(probs)




def CheckHomog(examples):
    classes = []
    for dictionary in examples:
        if dictionary['Class'] not in classes:
            classes.append(dictionary['Class'])
            if len(classes) > 1:
                return False
    return True



def ChooseAttribute(examples):
    keys = examples[0].keys()
    keys.remove('Class')
    scores = [entropy(examples,key) for key in keys]
    return keys[scores.index(min(scores))]




def Unique(examples,label):
    classes = []
    for example in examples:
        if example[label] not in classes:
            classes.append(example[label]) 
    return classes

def label_depth(node,track=0):
    node.depth = track
    if node.children != {}:
        for child in node.children:
            label_depth(node.children[child],track+1)



def ID3(examples,default=None):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  if examples == []:
      return Node(default)
  elif CheckHomog(examples):
      return Node(mode(examples))
  else:
      best = ChooseAttribute(examples)
      t = Node(default)
      t.attribute = best
      for label in Unique(examples,best):
          examples_i = [example for example in examples if example[best]==label]
          subtree = ID3(examples_i,mode(examples))
          t.add_child(label,subtree)
  label_depth(t)
  return t

             
def trimmer(node,max_depth):
    if node.depth == max_depth:
        node.children = {}
    else:
        for child in node.children:
            trimmer(node.children[child],max_depth)
    
    

def treeSize(node,track=0):
    if node.children == {}:
        return track
    track+=1
    branches = [treeSize(node.children[child],track) for child in node.children]
    return max(branches)


def prune(node, examples):
    '''
    Takes in a trained tree and a validation set of examples.  Prunes nodes in order
    to improve accuracy on the validation data; the precise pruning strategy is up to you.
    '''
    current_score = test(node,examples)
    improvement = 0
    while True:
        new_tree = copy.deepcopy(node)
        trimmer(new_tree,treeSize(node)-1)
        new_score = test(new_tree,examples)
        improvement =  new_score - current_score
        if improvement > 0:
            node = copy.deepcopy(new_tree)
        else:
            break
    return node



def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''
  total = len(examples)
  correct_count = 0
  for example in examples:
      y_true = example['Class']
      y_pred = evaluate(node,example)
      if y_true == y_pred:
          correct_count += 1
  return float(correct_count)/float(total)




def evaluate(node,example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
  if node.children=={} or example[node.attribute] not in node.children:
      return node.Ylabel
  
  attribute = node.attribute
  example_x = example[attribute]
  return evaluate(node.children[example_x],example)
