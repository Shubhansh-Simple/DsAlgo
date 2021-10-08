'''
Following operations code in linked list
done in this file

Traversal
Reverse
Deletion
Insertion
Showoff 2->3->4->5->None
'''

class Node:
    '''Each node have value and next reference to it.'''

    def __init__(self,value=None):
        self.value = value
        self.next  = None


class LinkedList:
    '''Linked List is just collection of node'''


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


    ##############
    # DELETION #
    ##############
    def remove( self, val):
        '''It's delete the value from singly linked list'''
    
        # SPECIALLY FOR HEAD
        if self.head.value == val:
            self.head = self.head.next
            return None

        temporary_head = self.head
        previous_value = None

        while temporary_head:
            # Way to iterate from the linked list
            
            if val == temporary_head.value:
                previous_value.next = temporary_head.next
                
                # SPEICALLY FOR TAIL
                if temporary_head == self.tail:
                    self.tail = previous_value

                return None

            previous_value = temporary_head
            temporary_head = temporary_head.next

        raise ValueError('Vale {} does not exist in list.'.format(val) )


    def insert(self,val):
        '''Insert node in linked list'''
        pass


n1 = Node(4)
n2 = Node(5)
n3 = Node(8)
n4 = Node(11)
n5 = Node(12)

ll = LinkedList()
ll.head = n1

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

ll.tail = n5


ll.showOff( ll.show() )
ll.reverse()
print('-----------------Reverse-----------------------')
ll.showOff( ll.show() )


remove_value = int( input('Type the value you want to remove - ') )
ll.remove(remove_value)
ll.showOff( ll.show() )

