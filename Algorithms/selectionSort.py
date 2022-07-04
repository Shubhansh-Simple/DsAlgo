from random import randrange

'''
Selection Sort Algorithm

Swapping the minimum element to the first

Time Complexity  - O(N^2)
Space Complexity - O(1)
'''


def selectionSort( arr ):
    '''Sort the given array using SELECTION SORT ALGORITHM'''

    if len(arr) < 2:
        return arr

    i = 0
    counter = 0
    while i < len(arr)-1:

        minimum = i                     # we assumming 'i' is minimum
        counter += 1

        # FINDING MINIMUM ELEMENT
        for j in range( i+1, len(arr) ):     # 'i' is dynamic here

            counter += 1
            if arr[j] < arr[minimum]:
                minimum = j            # storing index

        #print( arr[minimum], end=', ')


        arr[i], arr[minimum] = arr[minimum], arr[i] # swap

        #print( arr )
        i += 1

    print('Counter - ',counter)
    return arr              # sorted array


# INPUT
arr = [ randrange(20,50) for _ in range(10) ]
#arr.sort()


# OUTPUT
print('Array - ',arr)
print( 'Sorted - ',selectionSort( arr ) )
#arr.sort()
#print( 'Correct - ',arr )

'''
When array is nearly sorted Bubble Sort is very very efficient
algorithm as compare to selection sort algorithm
'''
