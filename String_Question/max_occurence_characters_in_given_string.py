'''
Finding the max occurence character
in the given string.
'''

sentence = 'I am good what about you ?'
string_counter = {}

def maxOccurence( string ):
    '''Find char which occurs max'''

    for x in string:
        try:
            string_counter[x] += 1
        except KeyError:
            if not x == ' ':
                string_counter[x] = 1
    return string_counter


'''
For finding maximum value
because dictionary don't maintain the sequence
but what if they are equal <--- 
'''

keyCounter,valueCounter = '',0

for key,value in (maxOccurence(sentence)).items():
    if valueCounter < value:
        keyCounter,valueCounter = key,value

print('{}:{}'.format(keyCounter,valueCounter) )




