import sys


def re_arrange(current_set, current_index):
	print(f"SET {current_index}")

	A = current_set[::2]
	B = current_set[1::2]
	B.reverse()
	for a in A:
		print(a)
	for b in B:
		print(b)
	




f = sys.stdin
current_set = []
current_index = 0

while True:
	# get number of people in this set
	n_set = int(f.readline().rstrip('\n'))

	if n_set == 0:
		break

	current_set = []
	current_index = current_index + 1
	for i in range(n_set):
		current_set.append(
			f.readline().rstrip('\n')
		)
	
	re_arrange(current_set, current_index)

