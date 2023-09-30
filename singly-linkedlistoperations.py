# Linked list operations in Python

# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_AtBeginning(self, new_data):
        #Allocate a new_node and assign data element
        new_node = Node(new_data)

        #make next node of new_node as head
        new_node.next = self.head

        #make new_node as head
        self.head = new_node

    def insert_AtPosition(self, position, new_data):
        # Create a new node
        new_node = Node(new_data)
        temp = self.head

        for i in range(1, position - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # Insert at the end
    def insert_AtEnd(self, new_data):
        #create a new_node
        new_node = Node(new_data)

        #if list is empty then make new_node as head
        if self.head is None:
            self.head = new_node
            return

        #else travel till the last node
        last = self.head
        while (last.next):
            last = last.next

        #change the next of last node
        last.next = new_node

    def delete_First(self):
        if (self.head != None):
            #if head is not null, create a temp node which points the head node
            temp = self.head

            #move head to next of head
            self.head = self.head.next

            #delete temp
            temp = None

    def delete_Last(self):
        if (self.head != None):
            # 1. if head in not null and next of head is null, release the head
            if (self.head.next == None):
                self.head = None
            else:
                # 2. Else, traverse to the second last element of the list
                temp = self.head
                while (temp.next.next != None):
                    temp = temp.next

                # 3. Change the next of the second last node to null
                # and delete the last node
                lastNode = temp.next
                temp.next = None
                lastNode = None

    # Deleting a node
    def delete_AtPosition(self, position):
        if self.head is None:
            return

        current = self.head

        for i in range(1, position):
            temp = current
            current = current.next

        if position == 1:
            self.head = self.head.next
        else:
            temp.next = current.next
            current = None

    # Search an element
    def search(self, key):
        #initialize current to head
        current = self.head

        #loop till current not equal to none
        while current is not None:
            if current.data == key:
                return True    #data found

            current = current.next
        return False  #data not found

    # Print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    print("\nlinked list : insert 1 at end:")
    llist.insert_AtEnd(1)
    llist.printList()

    print("\nlinked list : insert 2 at beginning:")
    llist.insert_AtBeginning(2)
    llist.printList()

    print("\nlinked list : insert 3 at beginning:")
    llist.insert_AtBeginning(3)
    llist.printList()

    print("\nlinked list : insert 4 at end:")
    llist.insert_AtEnd(4)
    llist.printList()

    print("\nlinked list : insert at position 3:")
    llist.insert_AtPosition(3,90)
    llist.printList()

    print("\nlinked list : delete first:")
    llist.delete_First()
    llist.printList()

    print("\nlinked list : delete last:")
    llist.delete_Last()
    llist.printList()

    print("\nAfter deleting at position 2:")
    llist.delete_AtPosition(2)
    llist.printList()

    print("\nPerforming Search :")
    item_to_find = 2
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found in the Linked List")
    else:
        print(str(item_to_find) + " is not found in the Linked List")