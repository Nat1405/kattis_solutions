import sys
def ends_w_99(bound):
    return str(bound)[-2:] == "99"

def get_bound(n):
    n = int(n)
    """
    My solution uses linear probing both
    above and below the given integer to
    return the first value that "ends in"
    99.
    """
    for i in range(100):
        lwr_bnd = n - i
        upr_bnd = n + i
        # eval upr_bnd first
        # to always return bigger
        if upr_bnd < 10000:
            if ends_w_99(upr_bnd):
                print(upr_bnd)
                break
        if lwr_bnd > 1:
            if ends_w_99(lwr_bnd):
                print(lwr_bnd)
                break

for n in sys.stdin:
    get_bound(n)
