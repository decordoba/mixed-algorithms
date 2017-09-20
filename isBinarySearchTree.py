"""
Function to check if a tree is a binary search tree.

RIGHT:
              8
          /       \
      4               C
    /   \           /   \
  2       6       A       E
 / \     / \     / \     / \
1   3   5   7   9   B   D   F


WRONG: (5 is grater than 2 but should be also smaller than 4)
      4
    /   \
  2       7
 / \     / \
1   5   6   8
"""

# Node class, every node will hold a value and a Left and Right child node
# Leaf nodes will have both children None
class Node:
    def __init__(self, val):
        self.val = val
        self.r = None
        self.l = None

    def __str__(self):
        return "Node: {}.   Children: ({}, {})".format(self.val,
                                                         None if self.l is None else self.l.val,
                                                         None if self.r is None else self.r.val)
    
# Recursive solution
def is_binary_search_tree_recursive(root_node, verbose=False):
    return check_node(root_node, verbose=verbose)
    
def check_node(node, min_val=None, max_val=None, verbose=False):
    if verbose:
        print(node)
        print("Min: {}, Max: {}".format(min_val, max_val))
    if (max_val is not None and node.val >= max_val) or (min_val is not None and node.val <= min_val):
        if verbose:
            print("This Node is not between the values {}-{}".format(min_val, max_val))
        return False
    if node.r is None and node.l is None:  # leaf node, no children
        if verbose:
            print("Leaf Node!")
        return True
    if node.l is not None:  # left has to be smaller than val
        new_max_val = node.val if max_val is None else min(node.val, max_val)
        if not check_node(node.l, max_val=new_max_val, min_val=min_val, verbose=verbose):
            return False
    if node.r is not None:  # right has to be grater than val
        new_min_val = node.val if min_val is None else max(node.val, min_val)
        if not check_node(node.r, max_val=max_val, min_val=new_min_val, verbose=verbose):
            return False
    return True

# Iterative solution
def is_binary_search_tree_iterative(root_node, verbose=False):
    queue = [(root_node, None, None)]
    while len(queue) > 0:
        node, max_val, min_val = queue.pop(0)  # removes first element queue
        if verbose:
            print(node)
            print("Min: {}, Max: {}".format(min_val, max_val))
        if (max_val is not None and node.val >= max_val) or (min_val is not None and node.val <= min_val):
            if verbose:
                print("This Node is not between the values {}-{}".format(min_val, max_val))
            return False
        if node.r is None and node.l is None:  # leaf node, no children
            if verbose:
                print("Leaf Node!")
        if node.l is not None:  # left has to be smaller than val
            new_max_val = node.val if max_val is None else min(node.val, max_val)
            queue.append((node.l, new_max_val, min_val))
        if node.r is not None:  # right has to be grater than val
            new_min_val = node.val if min_val is None else max(node.val, min_val)
            queue.append((node.r, max_val, new_min_val))
    return True
    
if __name__ == "__main__":
    # Create BST tree
    node2 = Node(2)
    node2.l = Node(1)
    node2.r = Node(3)
    node3 = Node(4)
    node3.l = node2
    node2 = Node(6)
    node2.l = Node(5)
    node2.r = Node(7)
    node3.r = node2
    
    root = Node(8)
    root.l =node3
    
    node2 = Node(10)
    node2.l = Node(9)
    node2.r = Node(11)
    node3 = Node(12)
    node3.l = node2
    node2 = Node(14)
    node2.l = Node(13)
    node2.r = Node(15)
    node3.r = node2
    
    root.r =node3

    verbose = False
    print("Recursive solution: The tree is a BST? {}\n".format(is_binary_search_tree_recursive(root, verbose=verbose)))
    print("Iterative solution: The tree is a BST? {}\n".format(is_binary_search_tree_iterative(root, verbose=verbose)))

    # Make tree not BST
    root.l.r.r.val = 9
    
    print("Recursive solution: The tree is a BST? {}\n".format(is_binary_search_tree_recursive(root, verbose=verbose)))
    print("Iterative solution: The tree is a BST? {}\n".format(is_binary_search_tree_iterative(root, verbose=verbose)))

# Solutions without verbose (easier to read)
"""
# Recursive solution
def is_binary_search_tree_recursive(root_node):
    return check_node(root_node)

def check_node(node, min_val=None, max_val=None):
    if max_val is not None and node.val >= max_val:
        return False
    if min_val is not None and node.val <= min_val:
        return False
    if node.r is None and node.l is None:  # leaf node, no children
        return True
    if node.l is not None:  # left has to be smaller than val
        new_max_val = node.val if max_val is None else min(node.val, max_val)
        if not check_node(node.l, max_val=new_max_val, min_val=min_val):
            return False
    if node.r is not None:  # right has to be grater than val
        new_min_val = node.val if min_val is None else max(node.val, min_val)
        if not check_node(node.r, max_val=max_val, min_val=new_min_val):
            return False
    return True

# Iterative solution
def is_binary_search_tree_iterative(root_node):
    queue = [(root_node, None, None)]
    while len(queue) > 0:
        node, max_val, min_val = queue.pop(0)  # removes first element queue
        if (max_val is not None and node.val >= max_val) or (min_val is not None and node.val <= min_val):
            return False
        if node.l is not None:  # left has to be smaller than val
            new_max_val = node.val if max_val is None else min(node.val, max_val)
            queue.append((node.l, new_max_val, min_val))
        if node.r is not None:  # right has to be grater than val
            new_min_val = node.val if min_val is None else max(node.val, min_val)
            queue.append((node.r, max_val, new_min_val))
    return True
"""