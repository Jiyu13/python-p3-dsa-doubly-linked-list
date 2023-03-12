class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:

    def __init__(self, head=None):
        self.head = head

    
    def append(self, node):
        # Add element to the beginning of the list if the list is empty
        if self.head == None:
            self.head = node
        
        # Otherwise, traverse the list to find the last node
        last_node = self.head:
        while last_node.next_node:
            
            # and add the node to the end
            # 1 -> 2 -> 3
            last_node = last_node.next_node
            # 1 -> 2 -> 3 -> 4


class SinglyLinkedListTrackTailNode:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    

    def append(self, node):
        # Add element to the beginning of the list if the list is empty
        if self.head == None:
            self.head = node
            self.tail= node
            return 

        # no need to traverse! we can access the last node directly (self.tail)
        # 1 -> 2 -> 3
        self.tail.next_node = node
        # 1 -> 2 -> 3 -> 4
        # we also need to make sure to keep track of the new tail

        self.tail = node