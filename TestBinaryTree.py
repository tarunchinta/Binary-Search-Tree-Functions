

#  File: TestBinaryTree.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:


import sys
import math


class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None
        self.empty = []

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()


    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    def minimum(self):
        current_node = self.root
        parent_node = current_node

        while current_node is not None:
            parent_node = current_node
            current_node = current_node.lChild
        
        return parent_node
    
    def maximum(self):
        current_node = self.root
        parent_node = current_node

        while current_node is not None:
            parent_node = current_node
            current_node = current_node.rChild
        
        return parent_node    
    
    def preorder (self, aNode, tempStr = []):
        if aNode:
            #print(aNode.data)
            tempStr.append(aNode)
            self.preorder(aNode.lChild, tempStr)
            self.preorder(aNode.rChild, tempStr)
        finalStr = []
        for i in tempStr:
            finalStr.append(i)
        return finalStr

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        if self.root is None:
            return None
        elif (self.root.lChild is None) and (self.root.rChild is None):
            return 0
        else:
            return (self.maximum().data - self.minimum().data)
        
    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        level_dict = {}
        num_of_levels = 10
        orderLst = []
        tempStr = []
        orderLst = self.preorder(self.root, tempStr)
        for i in range(num_of_levels):
            level_dict[i] = []
        for i in orderLst:
            try:
                level_dict[get_level_helper(self.root, i.data, 1) - 1].append(i)
            except KeyError:
                level_dict[get_level_helper(self.root, i.data, 1) - 1] = i

        return level_dict[level]

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        max_level = [0]
        lst = []
        return left_side_view_helper(self.root, 1, max_level, lst)

    
    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        lst = []
        sum_leaf_helper(self.root, lst)
        sum = 0
        for i in lst:
            sum += i
        return sum

def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree



#Adapted from G4G
def get_level_helper(root, val, level):
    #Base Case
    if (root is None):
        return 0
    #If we've found our level
    if (root.data == val):
        return level
    #Move one level down
    oneDown = get_level_helper(root.lChild, val, level + 1)
    if oneDown != 0:
        return oneDown
    oneDown = get_level_helper(root.rChild, val, level + 1)
    return oneDown


def sum_leaf_helper(root, lst = []):
    if root is None:
        return
    if (root.lChild is None) and (root.rChild is None):
        lst.append(root.data)
    sum_leaf_helper(root.lChild, lst)
    sum_leaf_helper(root.rChild, lst)
    return lst

#Adapted from G4G
def left_side_view_helper(root, level, max_level, lst = []):
    if root is None:
        return
    if (max_level[0] < level):
        lst.append(root.data)
        max_level[0] = level
    left_side_view_helper(root.lChild, level + 1, max_level, lst)
    left_side_view_helper(root.rChild, level + 1, max_level, lst)
    return lst



# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescope will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    total = 0
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())


    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")
# Another Tree
    total = 0
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print(f"All numbers on level 3 are {t3.get_level(3)}")
    print("##########################")

    print("#################################")
    t4 = make_tree([3,1,2,5,4])
    t4.print(t4.get_height())
    print(f"All numbers on level 2 are {t4.get_level(2)}")




if __name__ == "__main__":
    main()



