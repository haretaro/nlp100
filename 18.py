#sort -k 3 hightemp.txt
with open('hightemp.txt') as f:
    lines = f.readlines()
    lines.sort(key=lambda x: x.split()[2])
    print(''.join(lines))
