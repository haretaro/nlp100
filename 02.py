from functools import reduce
s1 = 'パトカー'
s2 = 'タクシー'
ans = reduce(lambda acc, x: acc + x,
        [a+b for a,b in zip(s1, s2)])
print(ans)
