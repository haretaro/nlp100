with open('hightemp.txt') as f:
    txt = f.read()
ans = txt.replace('\t', ' ')
print(ans)
