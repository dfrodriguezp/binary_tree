from node import *


class Tree(object):
    '''Tree object'''

    def __init__(self):
        self.root = None

    def add_value(self, val):
        '''Adds a value to the tree'''
        node = Node(val)
        if self.root == None:
            self.root = node
        else:
            self.root.add_node(node)

    def search(self, val):
        '''Returns the node where val is found,
        None otherwise'''
        return self.root.search(val)

    def traverse(self):
        '''Outputs the values of the
        nodes of the tree in ascending order'''
        self.root.visit()

    def info(self):
        '''Displays the data of the tree'''
        self.root.info()
