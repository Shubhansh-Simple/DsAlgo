class binaryTree:

    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


drinks = binaryTree('Drinks')
hot = binaryTree('Hot')
cold = binaryTree('Cold')
tea = binaryTree('Tea')
coffee = binaryTree('Coffee')
fanta = binaryTree('Fanta')
cola = binaryTree('Cola')

# Making Connections as Prev/Next

drinks.next = cold
drinks.prev = hot
cold.prev = cola
cold.next = fanta
hot.prev = tea
hot.next = coffee

# additional
#whiteTea = binaryTree('White Tea')
#blackTea = binaryTree('Black Tea')

nescafe = binaryTree('Nescafe')
bru = binaryTree('Bru')

#tea.prev = whiteTea
#tea.next = blackTea
coffee.prev = nescafe
coffee.next = bru

packets   = binaryTree('Packets')
container = binaryTree('Container')

nescafe.prev = packets
nescafe.next = container

maaza    = binaryTree('Maaza')
pepsi    = binaryTree('Pepsi')
thumbUp  = binaryTree('Thumb Up')

cola.prev = pepsi
cola.next = thumbUp
fanta.next = maaza
