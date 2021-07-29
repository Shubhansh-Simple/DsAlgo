'''
Reverse the string 
using recursion
'''
str_input = 'I am good what about you'

def stringReverser( string ):

    if len(string) == 1:
        return string

    return string[-1] + stringReverser(string[0:-1])


print('Original - ',str_input )
print('Reverser - ',stringReverser(str_input) )# calling function






