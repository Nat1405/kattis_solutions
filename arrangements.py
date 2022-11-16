import sys


def arrangements(N, M):
	"""
	We're doing this like a balls and bins problem. 
	Throw a ball into each bin, one bin at a time,
	until we no longer have any balls to throw.
	That's the idea anyways.
	"""
	t_div_r = M // N
	t_mod_r = M % N

	# For each room:
	for i in range(N):
		# Print base *'s per room
		for j in range(t_div_r):
			print('*', end='')
		# Print the extra if needed
		if i < t_mod_r:
			print('*', end='')
		print()


vals = sys.stdin.read().split('\n')
N = int(vals[0])
M = int(vals[1])
arrangements(N, M)