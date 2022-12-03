import sys
import itertools

n = int(sys.stdin.readline().rstrip('\n'))

def build_plank(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return build_plank(n-1)+build_plank(n-2)+build_plank(n-3)

print(build_plank(n))


