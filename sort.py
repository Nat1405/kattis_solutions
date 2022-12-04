import sys

# Get second line of input
line = sys.stdin.readline()
line = sys.stdin.readline().rstrip('\n')

ints = [int(x) for x in line.split(' ')]


# Calculate frequencies of ints
f = {}
for x in ints:
    try:
        f[x] += 1
    except KeyError:
        f[x] = 1

# Store index of first occurence
o = {}
for i, x in enumerate(ints):
    if x not in o:
        o[x] = i

def freq_first_occurance(x):
    return (-f[x], o[x])

a = sorted(ints, key=freq_first_occurance)

print(' '.join([str(x) for x in a]))

