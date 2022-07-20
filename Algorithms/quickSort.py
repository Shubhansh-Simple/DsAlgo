def isSorted( arr ):
    '''Return True/False weather sorted or not'''

    i = 0
    while i < len(arr)-1:
      if not arr[i] <= arr[i+1]:
        return False
      i += 1
    
    return True


def partition( arr, left, right ):
    '''
    Return pivot position
    Pivot Position - all elements left to it are smaller 
                     all elements right to it are greater
                     it's an fixed position for sorted array
    '''

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


def quicksort( arr, left, right ):
    '''Sort using Quick Sort algorithm'''

    # Array's LENGTH SHOULD BE GREATER THAN 2
    if left < right:

        pi = partition( arr, left, right )  # returns pivot index

        quicksort( arr, left, pi-1  )   # left  sub-array
        quicksort( arr, pi+1, right )   # right sub-array



from random import randrange
arr = [ randrange(1,15) for _ in range(10) ]

print('Array - ',arr )
quicksort( arr, 0, len(arr)-1 )
#print('Array - ',arr )

print( isSorted(arr) )




