sentence = 'this is the sentence'

def vowel_counter( string ):
    totalling = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'constant':0 }   # base

    for x in string:
        try:
            totalling[x] += 1
        except KeyError:
            if not x == ' ':
                totalling['constant'] += 1  # assuming spaces as constant

    return totalling

print('Ans - ',vowel_counter(sentence) )





