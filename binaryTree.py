
class Node:
    #A Node contains a data variable, a left, and a right reference
    def __init__(self, _data):
        self.data = _data
        self.left = None
        self.right = None

    def insert(self, data):
        #If the root Node is empty, assign data value
        if self.data is None:
            self.data = data

        #If given data value is less than current Node's data
        #Assign data to left variable IF it's empty
        #Else call left Node's insert() method
        elif data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)

        #If given data is higher than current Node's data
        #Assign data to right IF it's empty
        #Else call right Node's insert() method
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    #In-order prints tree values:
    #Left -> Parent -> Right
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


tree = Node(12)
tree.insert(11)
tree.insert(10)
tree.insert(14)
tree.insert(16)
tree.insert(20)
tree.insert(4)
tree.print_tree()

