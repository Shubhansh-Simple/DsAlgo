'''
We successfully able to create the linked list
using the normal python list

Also we test that list with our standard method 
it's working fine ;)
'''

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next  = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    ###############
    # SHOW OFF -> #
    ###############
    def showOff(self,data):
        '''It's shows the list in linked list format'''

        for x in data:
            print(x,end=' -> ')
        print('None')


    #############
    # ITERATING #
    #############
    def show(self):
        '''Returns entire linked list'''

        temporary_head = self.head
        temporary_list = []

        while temporary_head:
            temporary_list.append( temporary_head.value )
            temporary_head = temporary_head.next

        del temporary_head
        return temporary_list


    ##########
    # LENGTH #
    ##########
    def length(self):
        '''Returns the length of the linked list'''

        temporary_head = self.head
        counter = 0

        while temporary_head:
            counter += 1
            temporary_head = temporary_head.next
            
        return counter
        

    #############
    # REVERSING #
    #############
    def reverse(self):
        '''Just reverse the linked list'''

        temporary_head = self.head  # head means entire linked list

        for x in self.show()[::-1]:  # <--just remove the list right here

            temporary_head.value = x
            temporary_head = temporary_head.next

        return None

    ################################
    # CREATE LINKED LIST FROM LIST #
    ################################
    def createLinkedList( self, values ):
        '''Create linked list using given list'''

        if len(values) == 0:
            raise ValueError('Kindly pass a valid value')
        
        if len(values) == 1:
            n = Node( values )
            self.head = n
            self.tail = n

            # for breaking function
            return None

        i = 0
        previous = None

        while i < len(values):
    
            # Value should be the node
            n = Node( values[i] )

            # HEAD
            if i == 0:
                self.head = n

            # TAIL
            elif i == len(values)-1:
                self.tail = n
                n.next = None

            if previous:
                previous.next = n
            previous      = n

            i += 1

# Make a linked list using this list.
forLinkedList = [ 1, 2, 3, 4, 5 ]

ll = LinkedList()
ll.createLinkedList(forLinkedList)

print('Head, Tail - ',ll.head.value,ll.tail.value)
ll.showOff( ll.show() )

print('Length - ',ll.length() )

ll.reverse()
ll.showOff( ll.show() )

print('Head, Tail - ',ll.head.value,ll.tail.value)



















