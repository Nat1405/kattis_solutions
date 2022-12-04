import sys

bin_in = sys.stdin.readline().rstrip('\n')

# Pad with leading zeros

if len(bin_in)%3 != 0:
    bin_in = bin_in.zfill(len(bin_in) + (3 - (len(bin_in)%3)))

# Step through string with striiiiddddeesss!

output_str = ""
for i in range(0, len(bin_in), 3):
    chunk = bin_in[i:i+3]

    # Now for the big if/else table, since python 3.8 doesn't have
    # case/match statements
    if chunk == '000':
        output_str += '0'
    elif chunk == '001':
        output_str += '1'
    elif chunk == '010':
        output_str += '2'
    elif chunk == '011':
        output_str += '3'
    elif chunk == '100':
        output_str += '4'
    elif chunk == '101':
        output_str += '5'
    elif chunk == '110':
        output_str += '6'
    elif chunk == '111':
        output_str += '7'

print(output_str)

