from breadth_first import BinaryTree, Queue
import pytest

def test_add_four_nodes():
    tree = BinaryTree()
    tree.add('apples')
    tree.add('bananas')
    tree.add('cucumbers')
    tree.add('dates')
    assert tree._root.value == 'apples'
    assert tree._root.left.value == 'bananas'
    assert tree._root.right.value == 'cucumbers'
    assert tree._root.left.left.value == 'dates'
    assert tree._root.left.right == None


# Queue Tests
def test_queue_peek():
    q = Queue()
    q.enqueue('apples')
    assert q.peek() == 'apples'


def test_queue_peek_empty():
    q = Queue()

    with pytest.raises(IndexError):
        q.peek()


def test_is_empty_fresh():
    q = Queue()
    expected = True
    actual = q.is_empty()
    assert actual == expected


def test_is_not_empty_when_full():
    q = Queue()
    q.enqueue('spam')
    expected = False
    actual = q.is_empty()
    assert actual == expected


def test_is_empty_when_emptied():
    q = Queue()
    q.enqueue('spam')
    q.enqueue('eggs')
    q.dequeue()
    q.dequeue()
    expected = True
    actual = q.is_empty()
    assert actual == expected
