import sys

def rank_star_limit(n):
    '''star limits for each rank'''
    if 21 <= n and n <= 25:
        return 2
    elif 16 <= n and n <= 20:
        return 3
    elif 11 <= n and n <= 15:
        return 4
    elif 1 <= n and n <= 10:
        return 5
    # Since input only up to 10,000...
    elif n == 0:
        return 1000000

def move_up(rank, stars, n_stars):
    if rank == 0: # LEGEND!
        return 0, 0
    
    if stars + n_stars <= rank_star_limit(rank):
        return rank, stars+n_stars
    else:
        n_stars = n_stars - (rank_star_limit(rank) - stars)
        return rank-1, n_stars


def move_down(rank, stars):
    if rank == 0: # Can't touch the LEGENDS
        return 0, 0
    
    if stars > 0:
        return rank, stars-1
    else:
        if rank == 20:
            return rank, stars
        else:
            return rank+1, rank_star_limit(rank+1)-1


# Pad input with two losses, for the 'WWW' rule
input_str = 'LL' + sys.stdin.readline().rstrip('\n')

rank = 25
stars = 0

for i in range(2, len(input_str)):
    # get number of stars to add
    if input_str[i] == 'W':
        # Bonus stars!
        if rank >= 6 and input_str[i-2:i+1] == 'WWW':
            n_stars = 2
        else:
            n_stars = 1
        
        # Get new rank as function of new stars
        rank, stars = move_up(rank, stars, n_stars)
    else:
        if rank <= 20: # Doesn't affect ranks 20-25
            rank, stars = move_down(rank, stars)

if rank == 0:
    print("Legend")
else:
    print(rank)

