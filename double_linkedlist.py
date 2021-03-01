class DoubleLinkedListNode:
    #for interviewer reference
    def __init__(self, data, next=None, prev=None):
        self._data = data
        self._next = next
        self._prev = prev
    
class DoubleLinkedList:
    #for interviewer reference
    def __init__(self, head=None):
        self._head = head
        self._length = 0

    #function to implement
    def insert(self, data):
        #rather than using head as a parameter i used it as an attribute of the DoubleLinkedList class
        new_node = DoubleLinkedListNode(data)
        if self._head is None:
            self._head = new_node
        else:
            temp = self._head
            while temp._next is not None and temp._data <= new_node._data:
                temp = temp._next
            
            if temp._next is None:
                temp._next = new_node
                new_node._prev = temp
            else: 
                new_node._next = temp._next
                temp._next = new_node
                new_node._prev = temp
                new_node._next._prev = new_node

        self._length += 1
        return 
