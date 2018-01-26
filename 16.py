#split -n 5 hightemp.txt
import sys
import math
N = int(sys.argv[1])
with open('hightemp.txt') as f:
    lines = f.readlines()
n = math.ceil(len(lines)/N)
for i in range(N):
    with open('out{}'.format(i), 'w') as f:
        end = (i+1)*n if (i+1)*n < len(lines) else len(lines)
        f.write(''.join(lines[i*n: end]))
