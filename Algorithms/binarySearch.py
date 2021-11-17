'''
Binary Search algorithm
Find element - ele in array - arr
Array must be sorted
'''
def binarySearch( self, numbers, length, target, currentIndex ):
    start = 0
    end   = length-1
    
    while start <= end:
        
        mid = (start+end)//2
        if numbers[mid] == target:
            if mid == currentIndex:        # [ 1,2,3,4,4,9,56,90 ]  <-- HERE 4 is repeated yeah man.
                start = mid+1
            else:
                return mid                  # here mid is the index
        
        elif numbers[mid] < target:
            start = mid + 1
        
        else:
            end = mid-1
        
    return -1                           # because in case of 0, bool(0) <-- False

    
    

a = [ x for x in range(100000000) ]
ele = 99999999

'''
Non-binary Search takes 10 seconds

for x in a:
    if x == ele:
        print('Found')
        break
'''

# binary Search takes 4 seconds
ans = binarySearch(a,ele)

print('Ans - ',ans)
