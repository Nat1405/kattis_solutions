import sys


line = sys.stdin.readline().rstrip('\n')
line = line.split(' ')
n = int(line[0])
a = int(line[1])
b = int(line[2])
c = int(line[3])

print(f"{n} {a} {b} {c}")


def next_ride(n, a, b, c, prev):
    if n == 0:
        return 1

    # Symbolize choosing either a,b, or c for the next ride
    # What do we choose next? Can't choose previous, and 
    # can only choose from category where we have more rides available
    more_rides = 0
    if prev != 'a' and a > 0:
        more_rides += a*next_ride(n-1, a-1, b, c, 'a')
    if prev != 'b' and b > 0:
        more_rides += b*next_ride(n-1, a, b-1, c, 'b')
    if prev != 'c' and c > 0:
        more_rides += c*next_ride(n-1, a, b, c-1, 'c')
    
    return more_rides



print(next_ride(n, a, b, c, '') % (10e9+7))
