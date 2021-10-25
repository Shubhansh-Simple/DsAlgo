'''
Reverse
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


    def __str__(self):
        '''When you print the instance it will return this'''

        temporary_head = self.head
        all_node_values = []

        while temporary_head:
            all_node_values.append( str(temporary_head.value) )
            temporary_head = temporary_head.next

        return ' -> '.join( all_node_values )
   

    def reverse(self):
        '''Reverse the linked list by pointers'''

        temporary_node = self.head
        previous_node  = None

        while temporary_node:
            
            # just keep next_node as backup
            # that's it.

            next_node, temporary_node.next = temporary_node.next, previous_node

            previous_node  = temporary_node

            if not next_node:
                self.head = temporary_node

            temporary_node = next_node




n1 = Node(4)
n2 = Node(5)
n3 = Node(8)
n4 = Node(11)
n5 = Node(12)
n6 = Node(100)

ll = LinkedList()
ll.head = n1

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

ll.tail = n5

print(ll)
ll.reverse()
print(ll)


