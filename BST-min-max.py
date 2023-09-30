class Node:
    # A utility function to create a new node
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

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.data

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.data

# Driver program to test above function
if __name__ == '__main__':
    root = Node(10)
    root.insert(20)
    root.insert(8)
    root.insert(4)
    root.insert(6)

    print("Maximum value is :" , root.get_max())
    print("Minimum value is :", root.get_min())
