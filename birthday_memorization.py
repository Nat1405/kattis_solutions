import sys


def get_2d_list(unprocessed_friends_list):
	"""
	Start with entries like
		'Oden 78 03/12\n'
	and go to entries like
		[12, 3, 78, 'Oden']
	"""
	output = []
	for entry in unprocessed_friends_list:
		entry = entry.rstrip('\n').replace('/', ' ').split(' ')
		# Reverse the list
		entry.reverse()
		output.append(entry)

	return output


def process_friends_list(unprocessed_friends_list):
	"""
	whittle the friends down to those
	we will remember.
	"""

	# We will sort the friends by four keys.
	# 	1) birthday month
	#   2) birthday day
	#   3) friendship value
	#   4) lexicographic name

	# First we'll split the input strings to a form more amenable
	# to sorting.
	two_d_list = get_2d_list(unprocessed_friends_list)
	#print(two_d_list)

	sorted_two_d_list = sorted(
		two_d_list,
		key=lambda x: (int(x[0]), int(x[1]), int(x[2]), x[3])
	)


	# Finally remove duplicate (first two) entries
	final_output = {}
	for entry in sorted_two_d_list:
		reassembled_birthday = "/".join([entry[1], entry[0]])
		final_output[reassembled_birthday] = entry[3]

	# Judo CHOP to get the final result
	result = [final_output[key] for key in sorted(final_output.keys())]

	return result





# Outer loop, high-level organization
sys_in = sys.stdin.read()
split_input = sys_in.split('\n')
num_friends = int(split_input[0])
unprocessed_friends_list = split_input[1:num_friends+1]

#print(unprocessed_friends_list)

friends = process_friends_list(unprocessed_friends_list)

print(len(friends))
for f in sorted(friends):
	print(f)

