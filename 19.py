#coding: utf-8
#このコマンドでは出現頻度がわかるだけ
#cut -f 1 hightemp.txt | sort | uniq -c | sort -r

from itertools import groupby
with open('hightemp.txt') as f:
    lines = [line.split() for line in f.readlines()]
lines.sort(key=lambda x: x[0])
count = {k: len(list(j)) for k, j in groupby(lines, key=lambda x: x[0])}
lines.sort(key=lambda x: count[x[0]], reverse=True)
for line in lines:
    print('\t'.join(line))
