'''
Find the second largest/smallest
element in array
'''

array   = [1,5,47,40,21,2,8,15,3,18,58,55]

largest,second_largest  = 0,0  # initialization

'''
for x in array:
    if x > second_largest:
        if x < largest:
            second_largest = x 
        else:
            second_largest = largest
            largest = x
'''

for x in array:
    if x > largest:
        second_largest = largest
        largest = x

print('Largest value in array - ',largest)
print('Second Largest value in array - ',second_largest)




