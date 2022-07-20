'''
Second Largest Element without sorting entire array
'''


from random import randrange
arr = [ randrange(1,50) for _ in range(10) ] 


# ----------FIRST APPROACH----------  

# BUBBLE SORT ALGORITHM
# For finding the second largest element
for limit in range(1,3):

    i = 0
    while i < len(arr)-limit:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 1

print('Maximum - ', arr[-1] )
print('Second Maximum - ', arr[-2] )


#----------SECOND APPROACH---------- 
#Using Mini difference approach

maximum = max(arr)     # with O(n)
d = { maximum : 1 }    # for repeatition maxi element
diff = maximum

for x in arr:          # second traversal

    if x == maximum and d[maximum] == 1:
        d[maximum] -= 1

    elif diff > maximum-x:         # minimum difference
        diff = maximum-x


print('Largest - ',maximum )
print('Second largest - ',maximum-diff )


# for checking
arr.sort()
print( arr )











