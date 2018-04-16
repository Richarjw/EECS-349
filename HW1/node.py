class Node:
    def __init__(self):
        self.children = {}

    def decision_attribute(self,attribute):
        # Attribute this node cares about
        self.attribute = attribute

    def label(self,label):
        self.label = label
    
    def add_child(self, subtree):
        self.children.append(subtree) 
        
	# you may want to add additional fields here...