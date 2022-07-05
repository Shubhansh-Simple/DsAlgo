'''
Transfering the element from unsorted section to sorted section 
and maintain the sorted section sortedness while transfering 

             Sorted       UnSorted Section
[4,5,7,2] ->  [ 4, 5, 7 | 2 ]

Transfer 2 to the left side until we findout it's position  
( with comparision)

Time Complexity  - O(N^2)
Space Complexity - O(1)
'''

def insertionSort( array ):
    '''Sorting the arrayay using insertion sort algorithm.'''

    if len(array) < 2:
        return array

    i = 1
    while i < len(array):        # loop through array

        j = i

        # Swap the element to left 
        # until it found it's position
        # inside sorted array
        while array[j-1] > array[j] and j > 0:
            array[j], array[j-1] = array[j-1], array[j]   # swapping
            j -= 1
        i += 1

    return array                  # sorted arrayay



from random import randrange

arr = [ randrange(1,20) for _ in range(10) ]

arr1 = arr[:]            # pass by value or paas by reference ?

print( 'Array - ',arr )
print()
print( insertionSort(arr1) )




















