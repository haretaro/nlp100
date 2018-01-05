from random import sample
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

ans = ' '.join([w[0] + ''.join(sample(w[1:-1], len(w) -2)) +  w[-1] if len(w) > 4 else w for w in s.split()])
print(ans)
