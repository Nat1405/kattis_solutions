import sys


mod_values = []
for line in sys.stdin:
    if line == '\n':
        continue
    mod_values.append(int(line.rstrip('\n')) % 42)

print(len(set(mod_values)))

