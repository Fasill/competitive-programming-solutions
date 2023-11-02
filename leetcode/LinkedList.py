class Node:
    def __init__(self, data=None, next_node=None):
        # Initialize a node with data and a reference to the next node
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        # Initialize the linked list with a head node set to None
        self.head = None

    def insert_at_beginning(self, data):
        # Insert a new node at the beginning of the linked list
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        # Insert a new node at the end of the linked list
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)


    def print(self):
        # Print the linked list
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        list_str = ''

        while itr:
            list_str += str(itr.data) + ' --> '
            itr = itr.next
        print(list_str)

    def insert_values(self, data_list):
        # Insert a list of values into the linked list
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        # Get the length of the linked list
        if self.head is None:
            print(0)
            return
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(count)

    def remove_by_index(self, index):
        # Remove a node from the linked list based on the index
        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0
        while current:
            if count == index - 1:
                current.next = current.next.next
                return
            current = current.next
            count += 1

    def insert_at(self, index, value):
        # Insert a new node at a specific index in the linked list
        node = Node(value, self.head)
        if index == 0:
            self.head = node
            return

        current = self.head
        count = 0
        while current:
            if count == index - 1:
                node.next = current.next
                current.next = node
                return
            current = current.next
            count += 1

if __name__ == '__main__':
    # Create a linked list object and perform various operations
    li = LinkedList()

    li.insert_at_beginning(5)  # Insert at the beginning
    li.insert_at_beginning(81)  # Insert at the beginning
    li.insert_at_end(22)  # Insert at the end
    li.insert_values(["banana", "mango", "tie"])  # Insert a list of values
    li.insert_at(2, "hello")  # Insert at a specific index

    li.print()  # Print the final linked list
