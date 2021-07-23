'''
Find possible pairs of two numbers in given list
whose sum is lesser than the given number
'''

given_list = [ 1,3,7,9,10,11]
max_sum = 7

final_list =  []

for each_item in given_list:
    y = given_list.index(each_item) + 1

    for _ in range(len(given_list) - y):

        if each_item+given_list[y] < max_sum:
            final_list.append( (each_item,given_list[y]))
        y += 1

print('Numbers whose summation is less than 7 - ',final_list)

# Big O of this algorithm is O(n^2) 
# which is very bad yo.

