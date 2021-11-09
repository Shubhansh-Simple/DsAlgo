'''
Binary Search algorithm
Find element - ele in array - arr
Array must be sorted
'''

def binarySearch(arr,ele):
    '''We find the element in sorted arr in fastest way'''

    length = len(arr)

    start = 0             # first element
    end   = length-1      # last  element

    while start <= end:

        mid = (start+end)//2

        if arr[mid] == ele:
            return ele

        elif arr[mid] < ele:
            start = mid+1

        else:
            end = mid

    return -1
    

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
