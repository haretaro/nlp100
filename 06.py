def bigram(s):
    return set(s[i:i+2] for i in range(len(s)-1))
s1 = 'paraparaparadise'
s2 = 'paragraph'
X = bigram(s1)
Y = bigram(s2)
print('X', X)
print('Y', Y)
print('X | Y', X | Y)
print('X & Y', X & Y)
print('X - Y', X - Y)
print('se in X', 'se' in X)
print('se in Y', 'se' in Y)
