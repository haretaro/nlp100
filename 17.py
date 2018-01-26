#cut -f 1 hightemp.txt | sort | uniq
with open('hightemp.txt') as f:
    pref = list(set(line.split()[0] for line in f.readlines()))
    pref.sort()
    ans = '\n'.join(pref)
    print(ans)
