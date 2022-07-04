from random import randrange
'''
Time Complexity  - O(N^2)  # but not purely
Space Complexity - O(1)

Swap the array's adjancent element until
i reaches it's limit

Largest element reaches to end first         after O(N)
Second largest element reaches to end second after O(N+N)
soon

We can get the second largest array with O(N+N) time complexity

'''


def bubbleSort( arr ):
    '''Sort the array using bubble sort algrithm'''
    
    # SPECIAL CASE
    if len(arr) < 2:
        return arr

    i = 0
    while i < len(arr)-1:         # runs O(N) times

        stop = True
        j = 0

        while j < len(arr)-1-i:   # -i means removing last item from iteration
                                  # -1 means j+1 <-- with j
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] # swapping
                stop = False                      # arr not sorted

            j += 1

        if stop:                  # what if array is sorted completely before i
            return arr            # reaches to it's limit

        i += 1

    return arr

# INPUT
arr = [ randrange(0,20) for x in range(10) ]

# OUTPUT
print('Array - ',arr )
print('Sort - ',bubbleSort(arr) )

