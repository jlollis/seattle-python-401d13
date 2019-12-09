from collections import deque

class DoublyLinkedList:
    def __init__(self):
        self.dq = deque()

    def insert(self, value):
        return self.dq.appendleft('value')

    def remove_from_end(self):
        return self.dq.pop()
