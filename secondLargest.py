'''
Finding the second largest element in given array

Bubble Sort Approach
Minimum DIFFERENCE from max element approach
In-built Sorting approach
'''



# Generating Array
from random import randrange
arr = [ randrange(0,20) for x in range(10) ]
print( 'Array - ',arr )
####################
#   Solution Part  #
####################

# BUBBLE SORT APPROACH
for _ in range(2):
    i = 0
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 1

print('Second largest element - ',arr[-2])
print('-'*20)


########################################

# MINI DIFFERENCE FROM MAX(ELEMENT) APPROACH
def secondLargestUsingDiff( arr ):
    '''
    ELEMENT HAVE MINIMUM DIFFERENCE FROM MAX ELEMENT
    '''

    d = {}
    maximum = 0

    for x in arr:                # finding maximum element
        if x > maximum:
            maximum = x

        if d.get(x):             
            d[x] += 1
        else:
            d[x] = 1

    if d[maximum] > 1:           # what if max element appears 
        return maximum           # more than 1 times

    miniDiff = maximum

    for x in arr:                # that element who having minimum
        if not maximum-x == 0:   # difference from maximum element
            if maximum - x < miniDiff:
                miniDiff = maximum-x

    return maximum-miniDiff

print( secondLargestUsingDiff( arr ) )

########################################

# SORTIN ENTIRE ARRAY APPROACH
arr.sort()
print( 'Sorting approach - ',arr[-2] )


