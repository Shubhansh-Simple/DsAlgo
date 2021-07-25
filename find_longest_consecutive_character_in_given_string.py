current = 0
is_char_change = ''
d = {}

for x in 'AABCDDBBBBEA':
    if is_char_change == x:
        d[ x+str(current) ] += 1
    else:
        current += 1
        is_char_change = x

        try:
            d[ x+str(current) ]
        except KeyError:
            d[ x+str(current) ] = 1



# For finding the maximum value pairs
keyCounter,valueCounter = '',0

for key,value in d.items():
    if valueCounter < value:
        keyCounter,valueCounter = key,value

print('{}:{}'.format(keyCounter,valueCounter) )



