import random
import sys
import itertools

"""This solution is a modified solution of mine to industrial_spy.
It still uses the Miller-Rabin algorithm to check primality for
primes of up to 10e18, with minor input/output changes."""


def MR(n, k):
    """Implementation of the Miller-Rabin primality test.
        Inputs:
            - integer n, we will ensure it is greater than two and odd.
            - integer k, number rounds of testing to perform
        
        Pseudocode from 
    https://en.wikipedia.org/wiki/Miller–Rabin_primality_test#Example.
    
    Returns False if definitely composite, True if probably prime.
    """

    # First test to ensure n > 2 and n odd
    if n == 1:
        return False
    if n == 2:
        return True
    if (n % 2 == 0):
        return False
    if n == 3:
        return True

    # Now find s and d
    s, d = get_s_d(n)
    
    #print(f"N:\n{n}\nn-1 = (2**{s})*{d}")
    
    for _ in range(k):
        b = random.randint(2, n-2)
        #print(f"B: {b}")
        x = pow(b, d, n)
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and (x != n-1):
                return False
            x = y
        if y != 1:
            return False

    return True

def get_s_d(n):
    n_m_1 = n-1
    s = 0
    old_d = n_m_1
    old_r = 0
 
    # Implementation of do-while loop
    while True:
        d, r = divmod(old_d, 2)
        if r != 0:
            break
        s += 1
        old_d = d
        old_r = r

    return s, old_d


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip('\n'))

    # Uses miller-rabin algorithm with 20 iterations to check primality.
    # https://en.wikipedia.org/wiki/Miller–Rabin_primality_test
    if MR(n, 20):
        print("YES")
    else:
        print("NO")
