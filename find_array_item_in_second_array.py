'''
Just find if the item in first array
also present in the second array
'''

def itemChecker( arr1, arr2 ):
    '''Check weather the first array item prensent in second one.'''

    # assuming len(arr1) >= len(arr2)
    arr1_dict = {}
    for x in arr1:
        try:
            arr1_dict[x]
        except KeyError:
            arr1_dict[x] = True

    for y in arr2:
        try:
            arr1_dict[y]
            return True
        except KeyError: pass

    return False


array1 = [1,3,6]
array2 = [5,3,9]

print('Result is - ',itemChecker( array1,array2) )

#Big O of this approach - O(a+b)





