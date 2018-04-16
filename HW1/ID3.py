from node import Node
from parse import parse
import math


Data = parse("house_votes_84.data")  

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
	num_rep = 0
	num_dem = 0
	for item in examples:
		if item['Class'] == 'democrat':
			num_dem += 1
		elif item['Class'] == 'republican':
			num_rep += 1
	
	return 'republican' if num_rep > num_dem else 'democrat'

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
    ''' 
    given a name of a key in an entry in the examples list, return the entropy (assuming binary values)
    using formula H(Y) = - Sum ( pk * log_2(pk))
    '''

    num_yes = float(count_class(examples, name, 'y'))
    num_no = float(count_class(examples, name, 'n'))
    num_q = float(count_class(examples, name, '?'))
    total = num_yes + num_no + num_q
    
    prob_yes = float(num_yes/total)
    prob_no = float(num_no/total)
    prob_q = float(num_q/total)
    
    #where do we consider ?
    no_given_dem = compute_conditional_prob(examples, name, 'n','democrat')
    no_given_rep = compute_conditional_prob(examples, name,'n','republican')
    Hn = -no_given_dem - no_given_rep
	
    yes_given_dem = compute_conditional_prob(examples, name, 'y','democrat')
    yes_given_rep = compute_conditional_prob(examples, name,'y','republican')
    Hy = -yes_given_dem - yes_given_rep
	
    q_given_dem = compute_conditional_prob(examples, name,'?','democrat')
    q_given_rep = compute_conditional_prob(examples, name,'?','republican')
    Hq = -q_given_dem - q_given_rep
    
    IG = (-prob_no * Hn - prob_yes * Hy - prob_q * Hq) # only return this not prior, going to minimize this number
    return IG


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

def ID3(examples,default="Hell if I know"):
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
  return t

             
def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''
 

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
  
  
  

"""
Treat Unknown as if it's a whole new attribute

test case will involve a new category for an attribute not part of training data
"""

	
