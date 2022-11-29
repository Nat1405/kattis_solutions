import sys

if __name__ == "__main__":
    for line in sys.stdin:
        if line == '\n':
            break
        line = line.rstrip('\n')
        nums = line.split(' ')
        a = int(nums[0])
        b = int(nums[1])

        print(abs(a-b))

