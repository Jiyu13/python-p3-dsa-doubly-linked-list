class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head

    
    def delete_tail(self):
        if self.head == None:
            return 
        
        # traverse the entire list to find the second-to-last node (prev)
        curr = self.head
        prev = None
        while curr.next_node:
            prev = curr
            curr = curr.next_node
        # remove the last node by removing the link between the second-to-last node and the tail
        # 1 -> 2 -> 3
        prev.next_node = None
        # 1 -> 2