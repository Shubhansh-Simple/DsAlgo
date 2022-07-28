'''
Merge Sort Algorithm
Recursion Sequence is the way to understand merge sort

Divide the array into parts till the length become 1
then send first and second part for merging

'''

from shortcuts import colors

def mergeArray( arr, left, mid, right ):
    '''Merge two sorted array inside parent array using index'''

    i,j  = 0,0

    '''COPY DATA'''
    arr1 = arr[left:mid]     # sliced section is the 
    arr2 = arr[mid :right]   # sorted section of parent array


    #print('----------Merging Of Two arrays-----------')
    #print('Array1 - ',arr1)
    #print('Array2 - ',arr2)
    #print('------------------------------------------')

    counter = left           # initial position

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr[counter] = arr1[i] # modify parent array 
            i += 1

        else:
            arr[counter] = arr2[j] # modify parent array
            j += 1

        counter += 1 # every iteration

    # Merging Remaining Part     
    if i < len(arr1):
        arr[counter:right] = arr1[i:]
    else:
        arr[counter:right] = arr2[j:]

    '''No Return because we modify parent array'''
    del arr1, arr2



def mergeSort( arr, left, right ):
    '''Sort the array using merge sort algorithm'''

    #print( arr[left:right] )

    # Divide & Conquer whose length > 1
    if abs(left-right) > 1:                 # simple approach

        mid = (left+right) // 2

        mergeSort(arr, left, mid )          # divide left-subarray 
        mergeSort(arr, mid, right )         # divide right-subarray
        mergeArray( arr, left, mid, right ) # merge two sorted array



from random import randint


failure = 0
for counter in range(100000):
    
    arr = [ randint(0,90) for _ in range(randint(1,600)) ]
    
    #print('arr - ',arr)
    #print('Arr2 - ',arr2)
    
    answer = sorted( arr )
    
    mergeSort( arr, 0, len(arr) )   # sending length with -1 unlike quicksort   
    
    if not answer == arr:
        failure += 1
        input()

    if counter%100 == 0:
        print( f'{colors.BOLD}{counter}{colors.ENDC} {colors.GREEN}Test Case Passed{colors.ENDC}')
    
print('Total failure - ',failure )
