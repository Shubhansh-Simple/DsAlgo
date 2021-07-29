'''
Multiplication each array item
to each other using recursion
'''
item = [2,5,4,6]

def multiplyArrayItem( data ):
    if len(data) == 1:
        return data[0]

    return data[0] * multiplyArrayItem(data[1:])

print('Multiplication of ',item,' is ',multiplyArrayItem(item) )
    
    
