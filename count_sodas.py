import sys

def count_sodas(e, c):
    if e < c:
        return 0
    else:
        return e//c + count_sodas((e//c)+(e%c), c)

for line in sys.stdin:
    if line == '\n':
        continue
    line = line.rstrip('\n')

    e, f, c = line.split(' ')
    
    print(count_sodas(int(e) + int(f), int(c)))

