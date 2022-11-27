import random

def MR(n):
    """Implementation of the Miller-Rabin primality test. Given n:

        1) Compute s, d such that n-1 = (2^s)*d, (d%2)!= 0.
        2) Pick random b such that b is in [1, n-1]
        3) Computer (b^d % n), (b^(2^1)*d % n), ... (b^(2^s-1)*d % n)
            - Can be computed by repeatedly squaring previous result
              and taking remainder modulo n
        4) If any of those s numbers n-1, return n is prime. Else False.

    Main takaway: whenever this algo says n is not prime, it is correct.
    Only return that it is prime if over many runs it says prime.
    
    Pretty cool, very simple algorithm to have such profound results!
    """
    if n == 1 or (n % 2 == 0):
        return False

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
    
    print(f"N:\n{n}\nn-1 = (2**{s})*{old_d}")
    
    b = random.randint(1, n_m_1)

    print(f"B: {b}")

    # I am assuming s can't be 0, since we check if n is even
    nums = []
    
    acc = pow(b, old_d, n)

    nums.append(acc)
    for _ in range(s-1):
        acc = pow(acc, 2, n)
        nums.append(acc)

    results = [(x == n - 1) for x in nums]

    for num, result in zip(nums, results):
        print(f"{num}\n{result}")
    
    return any(results)


if __name__ == "__main__":
    MR(35201546659608842026088328007565866231962578784643756647773109869245232364730066609837018108561065242031153677)
