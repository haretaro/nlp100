import sys
N = int(sys.argv[1])
with open('hightemp.txt') as f:
    ans = "".join(f.readlines()[-N:])

print(ans)
