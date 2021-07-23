'''
Is there any pair in array
(without repeating & negative item)
whose summation is given sum_result
'''

array1 = [1,2,3,9,6]
array2 = [1,2,4,4]
sum_result = 8

def findPairs( arr1,sum_result ):
    '''Find pair whose summation is given sum'''

    found_pairs = []

    for x in arr1:
        substraction = abs( x-sum_result)  # to make it positive

        if substraction in found_pairs:
            return True
        else:
            found_pairs.append(x)

    return False # if nothing found


print( findPairs(array1,sum_result) )
print("------------------------------")
print( findPairs(array2,sum_result) )





