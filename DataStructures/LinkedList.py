# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # data 할당
        self.next = None  # Initialize next as null


# Linked List class
class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    # Function to insert a new node at the beginning
    def push(self, new_data):
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # Inserts a new node after the given prev_node.
    # This method is defined inside LinkedList class shown above
    def insertAfter(self, prev_node, new_data):

        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return

        # 2. Create new Node & 3. Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. make next of prev_node as new_node
        prev_node.next = new_node

    def append(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
    def deleteNode(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp is None:
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

    # Given a reference to the head of a list
    # and a position, delete the node at a given position
    def deleteNode2(self, position):
        if self.head is None:
            return

        if position == 0:
            self.head = self.head.next
            return self.head

        index = 0
        current = self.head
        prev = self.head
        temp = self.head

        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp

        return prev

    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
    def getCount(self):
        temp = self.head    # Initialise temp
        count = 0   # Initialise count

        # Loop while end of linked list is not reached
        while temp:
            count += 1
            temp = temp.next
        return count


if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second  # Link first node with second

    second.next = third  # Link second node with third
    llist.append(123)
    llist.deleteNode2(5)
    llist.printList()
