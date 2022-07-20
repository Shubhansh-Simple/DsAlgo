# UNCHANGED - SAME AS QUICKSORT ALGORIHTM
def partition( arr, left, right ):
    '''
    Return pivot position
    Pivot Position - all elements left to it are smaller 
                     all elements right to it are greater
                     it's an fixed position for sorted array
    '''
    
    # Debug
    #print( arr, ' | ',  arr[left:right+1] )

    pivot = right       # getting pivot each time
    right -= 1

    while not left == pivot:

        if left == right:
            if arr[left] > arr[pivot]:
                arr[left], arr[pivot] = arr[pivot], arr[left]
                break

        if arr[left] <= arr[pivot]:
            left += 1

        elif arr[right] > arr[pivot]:
            right -= 1

        else:
            arr[left], arr[right] = arr[right], arr[left]

    return left   # return pivot position


def quickselect( arr, left, right, search ):
    '''Search element in non-sorted array with sorted position'''

    '''
    Debug
    if left > right:
        #print( arr,' | ', arr[left:right+1] )
    '''

    # Where we need to compare - 1st
    if left == right == search-1:      # len( arr[left:right+1] ) is 1
        return arr[left]

    # Array's LENGTH SHOULD BE GREATER THAN 1
    if left < right:

        pi = partition( arr, left, right )  # returns pivot-index

        # BINARY SEARCH LIKE PARTITION
        if pi > search-1:
            return quickselect( arr, left, pi-1 , search ) #left sub-array

        elif pi < search-1:
            return quickselect( arr, pi+1, right, search ) #right sub-array

        else:
            # Where we need to compare - 2nd
            return arr[pi]


from random import randrange

arr = [ randrange(100,10000) for _ in range(10000) ]
arr1 = arr[:]

search = randrange(0,9999)

el = quickselect( arr, 0, len(arr)-1, search )
print('Your Answer   - ',el)

arr1.sort()
print('Actual Answer - ',arr1[search-1] )



