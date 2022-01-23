'''
Print all path of all leaf nodes
from ROOT node.
Successfully Accepted - leetcode
'''
class binaryTree:

    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


##################################################
n1 = binaryTree(1)
n2 = binaryTree(2)
n3 = binaryTree(3)
n4 = binaryTree(4)
n5 = binaryTree(5)
n6 = binaryTree(6)
n7 = binaryTree(7)
n8 = binaryTree(8)
n9 = binaryTree(9)
n10 = binaryTree(10)
n11 = binaryTree(11)
n12 = binaryTree(12)
n13 = binaryTree(13)
n14 = binaryTree(14)
n15 = binaryTree(15)
n16 = binaryTree(16)
n17 = binaryTree(17)
n18 = binaryTree(18)
n19 = binaryTree(19)
n20 = binaryTree(20)
n21 = binaryTree(21)

'''
n1.prev = n2
n1.next = n3
n2.next = n4
n4.prev = n5
n4.next = n6
n6.next = n8
n5.prev = n7
n5.next = n9
n9.prev = n10
'''
n1.prev = n2
n1.next = n3
n2.prev = n4
n2.next = n5
n4.prev = n8
n4.next = n9
n9.prev = n17
n9.next = n18
n8.next = n16
n5.prev = n10
n5.next = n11
n11.prev = n19
n3.prev = n6
n3.next = n7
n6.prev = n12
n6.next = n13
n12.next = n20
n7.prev = n14
n7.next = n15
n14.prev = n21

def rootToAllLeaf( root ):
    '''Using Pre-order traversal'''

    if root:
        
        # No Child
        if not root.prev and not root.next:
            return [str(root.data)]

        stack  = []
        output = []
        path   = {}
        result = []   # ['1->2->5','1->3' ]

        while True:
            output.append( str(root.data) )

            if root.prev:

                if root.next:
                    stack.append( root.next )
                    path[ root.next.data ] = output[:]  # copy

                root = root.prev

            elif root.next:
                root = root.next

            else:
                # LEAF NODE
                result.append( '->'.join(output) )
                #output.pop()

                if stack:
                    root   = stack.pop()
                    output = path[ root.data ]
                else:
                    break

        return result # answer

    else:
        return []

print( rootToAllLeaf( n1 ) )



















