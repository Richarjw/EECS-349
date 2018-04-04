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

def mode(examples):
	num_rep = 0
	num_dem = 0
	for item in examples:
		if item['Class'] == 'democrat':
			num_dem += 1
		elif item['Class'] == 'republican':
			num_rep += 1
	
	return 'republican' if num_rep > num_rep else 'democrat'
