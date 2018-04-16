class Node:
    def __init__(self,Ylabel):
        self.children = {}
        self.Ylabel = Ylabel

    def decision_attribute(self,attribute):
        # Attribute this node cares about
        self.attribute = attribute
    
    def add_child(self, label, node):
        self.children[label]=node

    def depth(self,level):
        self.depth = level