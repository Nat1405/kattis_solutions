import sys
import re

def my_less_equals(a, b):
    """Custom sorting function."""
    return a[:2] <= b[:2]


def merge(a, b):
    output = []

    i = 0
    j = 0
    while i != len(a) and j != len(b):
        if my_less_equals(a[i], b[j]):
            output.append(a[i])
            i += 1
        else:
            output.append(b[j])
            j += 1

    # Clean up
    while i < len(a):
        output.append(a[i])
        i += 1
    while j < len(b):
        output.append(b[j])
        j += 1

    return output


def my_sort(l):
    '''merge-sort with custom keys'''
    if len(l) <= 1:
        return l
    
    left = l[:len(l)//2]
    right = l[len(l)//2:]

    left = my_sort(left)
    right = my_sort(right)

    return merge(left, right)


if __name__ == "__main__":
    line = sys.stdin.readline().rstrip('\n')
    while line != '0':
        # Begin a new test case
        names = []
        for i in range(int(line)):
            names.append(sys.stdin.readline().rstrip('\n'))
        # print(names)

        for e in my_sort(names):
            print(e)
        line = sys.stdin.readline().rstrip('\n')
        if line != '0':
            print()




