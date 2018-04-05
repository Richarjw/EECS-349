from node import Node
from parse import parse
import math

Data = parse("house_votes_84.data")  

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  if examples == {}:
      return Node()
  elif "all examples have same classification or no non-trivial splits are available":
      return Node
  
         
def prune(node, examples):
  '''
  Takes in a trained tree and a validation set\ of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''

x = Node()
x.children = {"billy","joe"}

def entropy(examples,name):
	''' 
		given a name of a key in an entry in the examples list, return the entropy (assuming binary values)
		using formula H(Y) = - Sum ( pk * log_2(pk))
	'''
	num_yes = float(count_class(examples, name, 'y'))
	num_no = float(count_class(examples, name, 'n')) #need to consider ? here
	total = num_yes + num_no
	prob_yes = num_yes/total
	prob_no = num_no/total
	
	#where do we consider ?
	no_given_dem = compute_conditional_prob(examples, name, 'n','democrat')
	no_given_rep = compute_conditional_prob(examples, name,'n','republican')
	Hn = -no_given_dem - no_given_rep
	
	yes_given_dem = compute_conditional_prob(examples, name, 'y','democrat')
	yes_given_rep = compute_conditional_prob(examples, name,'y','republican')
	Hy = -yes_given_dem - yes_given_rep
	
	
	H = (-prob_no*Hn - prob_yes*Hy)
	return H

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
	
	return numerator / total

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
	
	return 'republican' if num_rep > num_rep else 'democrat'
