from node import *
from tree import *
from random import randint

tree = Tree()
for i in range(10):
    tree.add_value(randint(0, 100))
tree.traverse()

if tree.search(10):
    print(tree.search(10).info())
else:
    print("Value not found in the tree")
