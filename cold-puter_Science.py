import sys

def get_below_zero(temps):
	accumulator = 0
	a = temps.rstrip('\n')
	b = temps.split(' ')
	for t in b:
		if int(t) < 0:
			accumulator = accumulator + 1
	return accumulator


specs = sys.stdin.read()
temps = specs.split('\n')[1]

result = get_below_zero(temps)
print(result)
