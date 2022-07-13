'''
Bucket Sort - It uses an another sorting algorithm inside it's code
              When array's element is uniformly distributed
              ( means their difference is not very large )
'''
from random import randrange
from math   import sqrt,ceil


def bucketSort( arr ):
    '''Sort the array using bucket sort algorithm'''

    #No.of buckets for given array
    totalBuckets = round( sqrt(len(arr)) )           # formula

    # Making required buckets ( as per totalBuckets )
    buckets = []
    for _ in range( totalBuckets ):
        buckets.append([])            # matrix

    maximum = max(arr)                # O(N) 


    '''Destribution Of Elements 
       in respected buckets
       based on formula
    '''
    for x in arr:
        index = ceil( x * totalBuckets / maximum )   # formula
        buckets[ index-1].append(x)

    ''' 
    Sort elements in each buckets
    Then combine them one by one
    '''
    sortedArray = []
    i = 0
    while i < len(buckets):
        if buckets[i]:
            buckets[i].sort()             # Quicksort is best for this
            sortedArray += buckets[i]     # Combine bucket in sequence
        i += 1

    del buckets
    return sortedArray

# INPUTS
arr = [ randrange(1,10) for _ in range(10) ]

# OUTPUTS
print('Array - ',arr )
print('Sorted - ',bucketSort( arr ) )





