"""Performance comparison of Array, and LinkedLists
mprof run python main.py
"""
import timeit
from doubly_linked_list import DoublyLinkedList

ll = DoublyLinkedList()
arr = []

for n in range(100_000):
    ll.insert('eggs')
    arr.append('eggs')

def ll_insert():
    ll.insert('bacon')
    ll.remove_from_end()

def array_insert():
    arr.insert(0, 'bacon')
    arr.pop(0)


print('linked list', timeit.timeit(stmt=ll_insert, number=100_000))
print('array', timeit.timeit(stmt=array_insert, number=100_000))

