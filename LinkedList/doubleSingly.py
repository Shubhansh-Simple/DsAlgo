'''
Singly-Linked-List          DONE!
Circular-Singly-Linked-List Done!

START - Double Singly Linked List
------------------------
TRAVERSAL
SHOWOFF
LENGTH
SEARCH  ( SAME AS TRAVERSAL )
INSERT
REMOVE
REVERSE
------------------------
'''

class Node:

    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublySingly:

    def __init__(self):
        self.head = None
        self.tail = None


    def showOff( self, data ):
        '''Add -> (arrows) for showing linked list'''

        for x in data:
            print(x,end=' <=> ')
        print('None')


    def show(self):
        '''Return linked list values to python's list'''

        # LIST IS NONE
        if not self.head:
            return []

        # ONLY ONE ELEMENT
        if self.head == self.tail:
            return [ self.head.value ]

        # MORE THAN 1 ELEMENT
        temporary_head = self.head
        temporary_list = []

        while temporary_head:  # <-- MARK
            temporary_list.append( temporary_head.value )
            temporary_head = temporary_head.next 

        return temporary_list


    def length( self ):
        '''Returns the length of the doubly linked list'''

        counter = 0
        temporary_head = self.head

        while temporary_head:
            counter += 1
            temporary_head = temporary_head.next  # NONE at tail

        return counter


    def insert( self, val, location):
        '''INSERTION in DOUBLY linked list'''

        # NONE LIST
        if not self.head:
            raise ValueError('Value {} does not exist in list.'.format(val) )

        node = Node(val)
    
        # SINGLY NODE LIST
        if self.head == self.tail:

            # HEAD
            if location == 0:
                node.next = self.head
                self.head.prev = node
                self.head = node

                print('The value of tail - ',self.tail.value)
                return None

            # TAIL
            elif location == 1:
                self.head.next = node
                node.prev      = self.head
                self.tail      = node

                print('The value of head - ',self.head.value)
                return None

        # MORE THAN 1 NODE
        else:

            # HEAD
            if location == 0:
                node.next      = self.head
                self.head.prev = node
                self.head      = node
                return None

            # TAIL 
            elif location == 1:
                self.tail.next = node
                node.prev      = self.tail
                self.tail      = node
                return None

            # ANYWHERE IN THE LIST
            else:
                counter = 1
                temporary_head = self.head

                while not counter == location:

                    if temporary_head.next:
                        temporary_head = temporary_head.next

                    # ADDING EXCEPTION
                    else:
                        raise IndexError('Sequence index out of range')
                    counter += 1

                prev_node           = temporary_head.prev

                prev_node.next      = node
                node.prev           = prev_node
                node.next           = temporary_head
                temporary_head.prev = node

                return None


    def reverse(self):
        '''Reverse the DOUBLY linked list'''

        # NONE LIST
        if not self.head:
            return []

        # SINGL NODE LIST
        if self.head == self.tail:
            return [ self.head.value ]

        # MORE THAN ONE NODE

        reversed_node_values = self.show()

        i,temporary_head = len(reversed_node_values)-1, self.head
    
        # reverse the list using WHILE loop
        while i >= 0:
            
            temporary_head.value = reversed_node_values[i]

            # HEAD
            if i == 0:
                self.tail = temporary_head
           
            # TAIL
            elif i == len(reversed_node_values) - 1:
                self.head = temporary_head

            # NEXT NODE
            temporary_head       = temporary_head.next

            i -= 1

        print( self.head.value , self.tail.value )


    def remove( self, val ):
        '''It's remove the node from double linked list'''
       
        # EMPTY LIST
        if not self.head:
            raise ValueError('Value {} does not exist in list.'.format(val) )

        # SINGLY NODE LIST
        elif self.head == self.tail:
            if self.head.value == val:
                self.head, self.tail = None, None
            else:
                raise ValueError('Value {} does not exist in list.'.format(val))

        # MORE THAN ONE NODE
        else:

            # HEAD
            if self.head.value == val:
                self.head      = self.head.next
                self.head.prev = None

            # TAIL
            elif self.tail.value == val:
                self.tail      = self.tail.prev
                self.tail.next = None

            # ANYWHERE IN THE LIST
            else:
                temporary_head = self.head

                while temporary_head:
                    if temporary_head.value == val:
                        break
                    
                    # before reaching this line, code will break
                    temporary_head = temporary_head.next

                # do something.
                if temporary_head:
                    prev_node = temporary_head.prev
                else:
                    raise ValueError('Value {} does not exist in list.'.format(val))

                prev_node.next = temporary_head.next
                temporary_head.next.prev = prev_node

                return None


n1 = Node(8)
n2 = Node(10)
n3 = Node(7)
n4 = Node(30)

# next-prev
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3

dd = DoublySingly()
dd.head = n1
dd.tail = n4

dd.showOff( dd.show() )
print('Length - ',dd.length() )

#dd.insert(1000,6)
#dd.reverse()
dd.remove(30)

dd.showOff( dd.show() )
print('Length - ',dd.length() )




