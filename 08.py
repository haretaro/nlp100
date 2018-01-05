def cipher(s):
    return ''.join(chr(219 - ord(c)) if c.islower() else c for c in s)

s = 'I am an NLPer'

b = cipher(s)
print(b)
c = cipher(b)
print(c)
