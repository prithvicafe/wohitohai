# Binary Search Tree operations in Python

# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def printInorder(root):
   if root:
      # Traverse left subtree
      printInorder(root.left)

      # Visit node
      print(root.data, end=" ")

      # Traverse right subtree
      printInorder(root.right)


# calculates the inorder successor of the Node
def Inorder_Successor(node):
    current = node
    while(current.left is not None):
        current = current.left

    return current

def delete_node(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete_node(root.left, key)
    elif(key > root.data):
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = Inorder_Successor(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)

    return root

# Utility function to search a key in a BST
def search(root, find_data):
    # Base Cases: root is null or searched data is present at root
    if root is None or root.data == find_data:
        return root

    # searched data is greater than root's key
    if root.data < find_data:
        return search(root.right, find_data)

    # searched data is smaller than root's key
    return search(root.left, find_data)

if __name__ == '__main__':
    root = Node(10)
    root.insert(20)
    root.insert(8)
    root.insert(4)
    root.insert(6)

    print("Inorder traversal: ", end=' ')
    printInorder(root)

    print()
    print("delete node 4 :")
    delete_node(root,4)
    print()
    printInorder(root)

    print()
    print("Search node value 8 :")
    search_value = 8
    if search(root, search_value) is None:
        print("Not found")
    else:
        print("Found")

