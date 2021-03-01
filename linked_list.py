class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

class LinkedList:
    def __init__(self):
        self._first = None
        self._length = 0 

    def get_length(self):
        return self._length

    def add(self, value):
        if self._first is None:
            self._first = Node(value)
        else:
            temp = self._first
            while temp._next is not None:
                    temp = temp._next

            temp._next = Node(value)
    