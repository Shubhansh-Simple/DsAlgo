'''
--->Circular singly linked list<---
Singly Linked list done
Same thing what we done with the singly linked list

LENGTH
SHOW OFF
TRAVERSAL
REVERSE
SEARCH
DELETION
INSERTION
'''


class Node:

    def __init__(self,value=None):
        self.value = value
        self.next  = None


class CircularSingly:
    '''Singly linked list with tail next refer to the head'''


    def __init__(self):
        self.head = None
        self.tail = None


    def showOff(self,data):
        '''Show list in linked list format'''

        [ print(x,end=' -> ') for x in data ]
        print('None')


    def traversal(self):
        '''Just iterate through linked list and print value'''
    
        # MEANS - No node at all in linked list
        if not self.head:
            return []

        '''
        In SINGLY LINKED LIST
        the code of checking single node linked list :-

        if self.head == self.tail:
            # this means linked list have 
            # only one node

        '''

        # MEANS - Only one node in linked list
        if self.head.next == self.head:
            return [self.head.value]

        temporary_head = self.head
        nodeValues     = []

        while True:
            nodeValues.append( temporary_head.value )

            if temporary_head.next == self.head:
                # One iteration complete
                break

            temporary_head = temporary_head.next

        return nodeValues


    def length(self):
        '''Returns the length of the circular singly linked list'''

        # ZERO node in linked list
        if not self.head:
            return 0

        # FIRST node in linked list
        if self.head.next == self.head:
            return 1

        counter = 1
        temporary_head = self.head

        while not temporary_head.next == self.head:
            temporary_head = temporary_head.next
            counter += 1

        return counter


    def search( self, val ):
        '''Return the element if found in linked list.'''

        if not self.head:
            print('Empty List')
            return None

        if self.head.next == self.head:
            if self.head.value == val:
                return val
            else:
                raise ValueError('Value {} does exist in list'.format(val))


        temporary_head = self.head


        while not temporary_head.next == self.head:
            if val == temporary_head.value:
                return val
            temporary_head = temporary_head.next

        if temporary_head.value == val:
            return val
        
        raise ValueError('Value {} does exist in list'.format(val))


    def remove(self, val):
        '''Remove the item from the linked list'''

        # EMPTY LIST
        if not self.head:
            raise ValueError('Value {} does not found in list.'.format(val))

        # FOR HEAD
        if self.head.value == val:

            # CHECK, list contains only one element.
            if self.head.next == self.head:
                self.head, self.tail = None, None

            else:
                self.head      = self.head.next
                self.tail.next = self.head

            return None

        # FOR LOOKING ELEMENT
        else:
            previous_node  = None
            temporary_head = self.head

            while not temporary_head.next == self.head:

                # we FIND element
                if temporary_head.value == val:
                    previous_node.next = temporary_head.next
                    return None

                previous_node  = temporary_head
                temporary_head = temporary_head.next

            # FOR TAIL
            if temporary_head.value == val:
                previous_node.next = self.head
                self.tail          = previous_node
            else:
                raise ValueError('Value {} does not found in list.'.format(val))

    
    def insert(self, node, location):
        '''Insert the node inside linked list'''

        # EMPTY LIST
        if not self.head:
            node.next = node
            self.head = node
            self.tail = node
            return None

        # SINGLE ELEMENT
        if self.head.next == self.head:

            # HEAD
            if location == 0:
                node.next, self.head = self.head, node

                self.tail = node.next
                self.tail.next = self.head
                return None

            # TAIL
            elif location == 1:
                node.next = self.head
                self.tail.next, self.tail = node, node

                return None

        # ANYWHERE IN LIST
        else:
            # HEAD
            if location == 0:
                node.next,self.head = self.head,node
                self.tail.next = self.head

                return None
            
            # TAIL
            elif location == 1:
                node.next = self.head
                self.tail.next, self.tail = node, node

                return None

            # SPECIFIC LOCATION
            else:
                temporary_head = self.head
                previous_node  = None
                counter        = 1

                while not temporary_head.next == self.head:

                    if counter == location:
                        # we find that element.     
                        previous_node.next = node
                        node.next = temporary_head

                    previous_node  = temporary_head
                    temporary_head = temporary_head.next

                    counter += 1

                # tail is missing yeah man
                
    def reverse(self):
        '''Reverse the CIRCULAR-SINGLY linked list'''
       
        # EMPTY LIST
        if not self.head:
            return None

        # SINGLE NODE LIST
        elif self.head == self.head.next:
            return None

        # MORE THAN ONE NODE
        else:
            reversed_node_values, i = self.traversal()[::-1], 0
            temporary_head          = self.head

            while i < len(reversed_node_values):
               
                # reversing
                temporary_head.value = reversed_node_values[i]

                # HEAD
                if i == 0:
                    self.head      = temporary_head
                    self.tail.next = self.head

                # TAIL
                elif i == len(reversed_node_values)-1:

                    self.tail      = temporary_head
                    self.tail.next = self.head


                temporary_head = temporary_head.next
                i += 1






n1 = Node(4)
n2 = Node(5)
n3 = Node(9)
n4 = Node(11)
n5 = Node(22)

n6 = Node(1000)

ll = CircularSingly()
ll.head = n1
ll.tail = n5

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n1

print()
ll.showOff( ll.traversal() ) 
print('Length -',ll.length() )

# FOR SEARCH
#print( 'Match found - ',ll.search(9) )

# REVERSE method also added

'''
print()
ll.remove(22)
ll.showOff( ll.traversal() ) 
print('Length -',ll.length() )
'''

print()
print('Length -',ll.length() )
ll.insert(n6,1)
ll.showOff( ll.traversal() ) 
print('Length -',ll.length() )

########################################



