def n_gram(s, n):
    return [s[i:i+n] for i in range(len(s)-n+1)]

s = 'I am an NLPer'
w_bigram = n_gram(s.split(), 2)
print(w_bigram)
c_bigram = n_gram(s.replace(' ',''), 2)
print(c_bigram)
