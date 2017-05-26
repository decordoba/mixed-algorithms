"""
Trivial challenge I had to answer in my interview with drive.ai (I did not receive an offer,
so I guess I was not great in my responses, but still the question and algorithm were
really easy). The idea was to get a tree root, with several children which would also have
more children, and print these children separated by comas, according to their depth in the
tree. See the example:

Input:
  A
 / \
B   C
|  /|\
D E F G
|   |\
H   I J

Output:
A
B, C
D, E, F, G
H, I, J
"""

class Node(object):
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

def print_levels(root_node):
    q = [root_node]
    stdout = ""
    children = 1
    while len(q) > 0:
        el = q.pop(0)
        stdout += el.val
        children -= 1
        for c in el.children:
            q.append(c)
        if children == 0:
            print stdout
            stdout = ""
            children = len(q)
        else:
            stdout += ", "

def create_example_tree():
    H = Node("H")
    I = Node("I")
    J = Node("J")
    
    D = Node("D", [H])
    E = Node("E")
    F = Node("F", [I, J])
    G = Node("G")
    
    B = Node("B", [D])
    C = Node("C", [E, F, G])
    
    A = Node("A", [B, C])
    
    return A

if __name__ == "__main__":
    root = create_example_tree()
    print_levels(root)
