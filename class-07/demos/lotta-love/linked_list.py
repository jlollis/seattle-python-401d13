class LinkedList:
    """[summary]
    Don't Forget you DocString!
    Returns:
        [type] -- [description]
    """
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):

        current = self.head

        while current:
            if current.value == value:
                return True

            current = current.next

        return False

    def __str__(self):
        as_string = 'LinkedList : '
        current = self.head
        while current:
            as_string += f'[{current.value}] -> '
            current = current.next


        return as_string





class Node:
    """[summary]
    Don't Forget you DocString!
    Returns:
        [type] -- [description]
    """
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


##################################################
## Side Note:                       ##############
## Implicit Inhertance from built in object ######
##################################################

class Animal(object): # absolutely no difference from class Animal:
    pass

class Mammal(Animal):
    pass

class Human(Mammal):
    pass


##################################################
## Built in Tests, no PyTest needed        #######
##################################################

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert('apples')
    assert ll.head.value == 'apples'
    ll.insert('bananas')

    print(ll)

    assert ll.head.value == 'bananas'
    assert ll.head.next.value == 'apples'
    assert ll.head.next.next == None

    assert ll.includes('bananas') == True
    assert ll.includes('apples') == True
    assert ll.includes('zucchinni') == False

    ll = LinkedList()
    assert ll.includes('bananas') == False


    print('tests passed!!!!!')







