import sys
N = int(sys.argv[1])
with open('hightemp.txt') as f:
    for row in f.readlines()[-N:]:
        print(row.rstrip('\n'))
