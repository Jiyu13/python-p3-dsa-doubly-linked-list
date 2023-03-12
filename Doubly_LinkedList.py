class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node



class DoublyLinkedList1:

    def __init__(self, head=None, tail=None):
        self.head = head

    
    def delete_tail(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # traverse the entire list to find the second-to-last node (prev)
        else:
            # access the second-to-last node (self.tail.prev_node)
            prev = self.tail.prev_node
            # update the tail and next_node pointers
            # 1 <-> 2 <-> 3  

            prev.next_node = None
            self.tail = prev
            # 1 <-> 2


class DoublyLinkedList2:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, node):
        if self.head = None:
            self.head = node
            self.tail = node
            return 
        
        node.prev_node = self.tail
        self.tail.next_node = node
        self.tail = node



ls = DoublyLinkedList2()
ls.append(Node("bulldog"))

ls.append(Node("chihuahua"))

ls.append(Node("german sheperd"))