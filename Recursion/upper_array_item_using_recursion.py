'''
Upper each item 
of the array 
using recursion
'''
arr = [ 'one','two','three','four' ]

def upperArrayItem( data ):
    #for x in arr:
    #    new_arr.append(x.upper())
    #return new_arr
    if len(data) == 1:
        return [data[0].upper()]

    return [data[0].upper()] + upperArrayItem(data[1:])  # recursion

print('Array - ', upperArrayItem( arr ) )




