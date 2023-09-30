class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct_tree(postfix):
    stack = []
    for ch in postfix:
        if ch.isalpha():
            new_node = Node(ch)
            stack.append(new_node)
        else:
            new_node = Node(ch)
            new_node.right = stack.pop()
            new_node.left = stack.pop()
            stack.append(new_node)
    return stack.pop()

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


postfix = "ABC*+D/"

root = construct_tree(postfix)
print("Inorder traversal of expression tree:")
inorder(root)