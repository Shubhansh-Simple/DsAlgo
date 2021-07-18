'''
Sort combined list of
two sorted list
'''

def sorter(li1,li2):
    '''assuming len(li1) >= len(li2)'''

    final_list = []            # final sorted list
    li1_index, li2_index = 0,0 # initial
    
    while True:
        try:
            if li1[li1_index] < li2[li2_index]:
                final_list.append( li1[li1_index] )
                li1_index += 1
            else:
                final_list.append( li2[li2_index] )
                li2_index += 2

        except IndexError:
            # add remaining part to the final list
            final_list += li1[li1_index:]
            break


    return final_list

li1 = [ 1,5,6,9,10,12,15]
li2 = [ 2,3,4,7,8,11,13,14]

# just passing big list first
print('Final sorted list - ',sorter(li2,li1) )









