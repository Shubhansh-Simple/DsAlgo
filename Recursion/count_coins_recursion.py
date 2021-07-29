'''
Count mininum no.of coins 
to complete given amount
without using recursion
'''
def coinsToFullFillAmt( amt ):
    final_list = []

    while True:
        if amt == 0:
            return final_list,len(final_list)

        elif amt >= 10:
            amt -= 10
            final_list.append(10)  # hard coded

        elif amt >= 5:
            amt -= 5
            final_list.append(5)

        elif amt >= 2:
            amt -= 2
            final_list.append(2)

        elif amt == 1:
            amt -= 1
            final_list.append(1)

dataReturn = coinsToFullFillAmt(59)

print('Total',dataReturn[1],'coins of ',dataReturn[0] )


