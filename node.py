class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def visit(self):
        if self.left != None:
            self.left.visit()
        print(self.value)
        if self.right != None:
            self.right.visit()

    def search(self, val):
        if self.value == val:
            return self
        elif val < self.value and self.left != None:
            return self.left.search(val)
        elif val > self.value and self.right != None:
            return self.right.search(val)
        return None

    def add_node(self, node):
        '''Adds a node to the tree'''
        if node.value < self.value:
            if self.left == None:
                self.left = node
            else:
                self.left.add_node(node)
        elif node.value > self.value:
            if self.right == None:
                self.right = node
            else:
                self.right.add_node(node)

    def info(self):
        '''Displays the information of the node'''
        print(self.__dict__)
        if self.left != None:
            self.left.info()
        if self.right != None:
            self.right.info()
