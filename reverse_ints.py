import sys

lines = []
for i, line in enumerate(sys.stdin):
    if i == 0 or line == '\n':
        continue
    line = int(line.rstrip('\n'))
    lines.append(line)

lines.reverse()

for l in lines:
    print(l)

