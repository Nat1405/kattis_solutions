import sys



def get_moves(*args):
    '''
    Get moves for a, given a's type and position,
    and that a belongs to team a attacking team b.
    '''
    a_type = args[0]
    
    moves = []
    # Check each of the eight linear directions,
    # With constraints for the various pieces.
    if a_type[0].lower() == 'k':
        moves.extend(check_right(*args, limit=1))
        moves.extend(check_upper_right(*args, limit=1))
        moves.extend(check_up(*args, limit=1))
        moves.extend(check_upper_left(*args, limit=1))
        moves.extend(check_left(*args, limit=1))
        moves.extend(check_lower_left(*args, limit=1))
        moves.extend(check_down(*args, limit=1))
        moves.extend(check_lower_right(*args, limit=1))
    elif a_type[0].lower() == 'q':
        moves.extend(check_right(*args))
        moves.extend(check_upper_right(*args))
        moves.extend(check_up(*args))
        moves.extend(check_upper_left(*args))
        moves.extend(check_left(*args))
        moves.extend(check_lower_left(*args))
        moves.extend(check_down(*args))
        moves.extend(check_lower_right(*args))
    elif a_type[0].lower() == 'b':
        moves.extend(check_upper_right(*args))
        moves.extend(check_upper_left(*args))
        moves.extend(check_lower_left(*args))
        moves.extend(check_lower_right(*args))
    elif a_type[0].lower() == 'r':
        moves.extend(check_right(*args))
        moves.extend(check_up(*args))
        moves.extend(check_left(*args))
        moves.extend(check_down(*args))
    elif a_type[0].lower() == 'n':
        moves.extend(check_l((-1, -2), *args))
        moves.extend(check_l((-1, 2), *args))
        moves.extend(check_l((1, -2), *args))
        moves.extend(check_l((1, 2), *args))
        moves.extend(check_l((-2, -1), *args))
        moves.extend(check_l((2, -1), *args))
        moves.extend(check_l((-2, 1), *args))
        moves.extend(check_l((2, 1), *args))
    elif a_type[0].lower() == 'p':
        moves.extend(get_pawn_moves(*args))
    else:
        raise NotImplementedError()

    return moves

def get_pawn_moves(
        p_type,
        p_pos,
        a_pieces,
        b_pieces,
        limit=None):
    # First, pawns move either up or down depending on colour.
    if p_type[0].isupper():
        # White pieces move up the board
        direction = -1
    else:
        direction = 1

    # Pawns can either move one forward, two forward at start,
    # or diagonally to attack. Don't worry about en passant.
    # Promotion is not handled here, it's handled after the
    # move is made.
    moves = []

    occupied_squares = list(a_pieces.values())
    occupied_squares.extend(list((b_pieces).values()))

    # Check for forward move; can only do if empty
    forward_move = (p_pos[0] + direction, p_pos[1])
    if forward_move not in occupied_squares:
        moves.append(forward_move)

    # Check for two-forward move
    if (p_pos[0] == 1 and p_type[0] == 'p') or \
        (p_pos[0] == 6 and p_type[0] == 'P'):
        double_forward_move = (p_pos[0] + 2*direction, p_pos[1])
        if double_forward_move not in occupied_squares and \
            forward_move not in occupied_squares:
            moves.append(double_forward_move)

    # Check for attacking moves
    attack_move_left = (p_pos[0] + direction, p_pos[1]-1)
    attack_move_right = (p_pos[0] + direction, p_pos[1]+1)
    if attack_move_left in b_pieces.values():
        moves.append(attack_move_left)
    if attack_move_right in b_pieces.values():
        moves.append(attack_move_right)

    return moves


def check_right(*args, **kwargs):
    # i ranges from 0 to 1 with step of 1,
    # j ranges from 1 to 8 with step of 1
    return straight_line_check((0, 1, 1), (1, 8, 1), *args, **kwargs)

def check_up(*args, **kwargs):
    # i ranges from -1 to -8 with step of -1,
    # j ranges from 0 to 1 with step of 1
    return straight_line_check((-1, -8, -1), (0, 1, 1), *args, **kwargs)

def check_left(*args, **kwargs):
    # i ranges from 0 to 1 with step of 1,
    # j ranges from -1 to -8 with step of -1
    return straight_line_check((0, 1, 1), (-1, -8, -1), *args, **kwargs)

def check_down(*args, **kwargs):
    # i ranges from 1 to 8 with step of 1,
    # j ranges from 0 to 1 with step of 1
    return straight_line_check((1, 8, 1), (0, 1, 1), *args, **kwargs)

def check_upper_right(*args, **kwargs):
    # i and j have same absolute value but sometimes one is negative
    return diagonal_check((-1,-8,-1), (1,8,1), *args, **kwargs)

def check_upper_left(*args, **kwargs):
    # i and j have same absolute value but sometimes one is negative
    return diagonal_check((-1,-8,-1), (-1,-8,-1), *args, **kwargs)

def check_lower_left(*args, **kwargs):
    # i and j have same absolute value but sometimes one is negative
    return diagonal_check((1,8,1), (-1,-8,-1), *args, **kwargs)

def check_lower_right(*args, **kwargs):
    # i and j have same absolute value but sometimes one is negative
    return diagonal_check((1,8,1), (1,8,1), *args, **kwargs)


def diagonal_check(
        i_range,
        j_range,
        p_type,
        p_pos,
        a_pieces,
        b_pieces,
        limit=None
    ):
    moves = []
    x, y, z = i_range
    u, v, w = j_range
    for i, j in zip(range(x, y, z), range(u, v, w)):
        if limit:
            if abs(i) > 1 or abs(j) > 1:
                continue
        new_pos = (p_pos[0]+i, p_pos[1]+j)
        # Now, stop extending for a variety of reasons.
        # If out of bounds, stop extending.
        if (new_pos[0] < 0) or (new_pos[0] > 7) or \
                (new_pos[1] < 0) or (new_pos[1] > 7):
            return moves

        # If hit your own piece, stop extending.
        if new_pos in a_pieces.values():
            return moves
        
        # # If hit an opponent, take the move and stop extending.
        if new_pos in b_pieces.values():
            moves.append(new_pos)
            return moves
        
        moves.append(new_pos)
    return moves


def straight_line_check(
        i_range,
        j_range,
        p_type,
        p_pos,
        a_pieces,
        b_pieces,
        limit=None,
    ):
    '''Checks a single linear direction'''
    moves = []
    x, y, z = i_range
    u, v, w = j_range
    for i in range(x, y, z):
        for j in range(u, v, w):
            # Apply king limit if need be
            if limit:
                if abs(i) > 1 or abs(j) > 1:
                    continue
            new_pos = (p_pos[0]+i, p_pos[1]+j)
            # print(new_pos)
            # print(new_pos)
            # if new_pos in a_pieces.values():
            #     print("foo")
            # else:
            #     print(f"{new_pos}: {a_pieces.values()}")
            # Check in bounds and not colliding with any other pieces
        
            # Now, stop extending for a variety of reasons.
            # If out of bounds, stop extending.
            if (new_pos[0] < 0) or (new_pos[0] > 7) or \
                    (new_pos[1] < 0) or (new_pos[1] > 7):
                return moves

            # If hit your own piece, stop extending.
            if new_pos in a_pieces.values():
                return moves
            
            # # If hit an opponent, take the move and stop extending.
            if new_pos in b_pieces.values():
                moves.append(new_pos)
                return moves
            
            moves.append(new_pos)
    
    return moves

def check_l(
        jumps,
        p_type,
        p_pos,
        a_pieces,
        b_pieces,
        limit=None
    ):
    # Check the horse moves ie jumps
    i, j = jumps
    moves = []
    new_pos = (p_pos[0]+i, p_pos[1]+j)
    # If out of bounds, stop extending.
    if (new_pos[0] < 0) or (new_pos[0] > 7) or \
            (new_pos[1] < 0) or (new_pos[1] > 7):
        return moves

    # If hit your own piece, stop extending.
    if new_pos in a_pieces.values():
        return moves
        
    moves.append(new_pos)
    return moves

def f(coords):
    '''Transform thing like (0, 0) to (8, a)'''
    i = chr(97+coords[1])
    j = 8 - coords[0]
    return str(i)+str(j)


def a_mates_b(a_pieces, b_pieces):
    '''Look for a checkmate
    b's king is in range of one of a's pieces, and
    no possible move by b can prevent it.
    '''

    # Try all possible moves to save the king
    for b_type, b_pos in b_pieces.items():
        moves = get_moves(b_type, b_pos, b_pieces, a_pieces)
        for m in moves:
            # Get the new game board after moving the black piece
            new_b_pieces = dict(b_pieces)
            new_b_pieces.pop(b_type)
            # Don't worry about promotion in cases of checkmate
            new_b_pieces[b_type] = m
            
            # Account for capture
            new_a_pieces = dict(a_pieces)
            for a_type, a_pos in a_pieces.items():
                if a_pos == m:
                    new_a_pieces.pop(a_type)

            # If in this new game board a doesn't threaten the king,
            # you've found a way out. Return False.

            # Recalculate the b_king position and possible moves for a
            try:
                b_king_pos = new_b_pieces['K']
            except KeyError:
                b_king_pos = new_b_pieces['k']

            all_moves_a = []
            for a_type, a_pos in new_a_pieces.items():
                # if a_type[0] == 'N' and new_b_pieces['k'] == (1, 5):
                #     print("HERE")
                #     print(a_pieces)
                #     print(new_b_pieces)
                #     print(get_moves(a_type, a_pos, a_pieces, new_b_pieces))

                all_moves_a.extend(get_moves(a_type, a_pos, new_a_pieces, new_b_pieces))

            if b_king_pos not in all_moves_a:
                #print(new_b_pieces)
                #print(all_moves_a)
                #print(f"Saving move: {b_pos} {m}")
                return False

    return True


if __name__ == "__main__":
    w_pieces = {}
    b_pieces = {}
    
    # Need unique keys for each piece
    w_pawns = 0
    w_rooks = 0
    w_bishops = 0
    w_knights = 0
    w_queens = 0
    b_pawns = 0
    b_rooks = 0
    b_bishops = 0
    b_knights = 0
    b_queens = 0

    for i in range(8):
        line = sys.stdin.readline().rstrip('\n')
        chars = list(line)
        for j, c in enumerate(chars):
            # White pieces
            if c == 'P':
                w_pieces[c+str(w_pawns)] = (i, j)
                w_pawns += 1
            if c == 'N':
                w_pieces[c+str(w_knights)] = (i, j)
                w_knights += 1
            if c == 'B':
                w_pieces[c+str(w_bishops)] = (i, j)
                w_bishops += 1
            if c == 'R':
                w_pieces[c+str(w_rooks)] = (i, j)
                w_rooks += 1
            if c == 'Q':
                w_pieces[c+str(w_queens)] = (i, j)
                w_queens += 1
            if c == 'K':
                w_pieces[c] = (i, j)
            
            # Black pieces
            if c == 'p':
                b_pieces[c+str(b_pawns)] = (i, j)
                b_pawns += 1
            if c == 'n':
                b_pieces[c+str(b_knights)] = (i, j)
                b_knights += 1
            if c == 'b':
                b_pieces[c+str(b_bishops)] = (i, j)
                b_bishops += 1
            if c == 'r':
                b_pieces[c+str(b_rooks)] = (i, j)
                b_rooks += 1
            if c == 'q':
                b_pieces[c+str(b_queens)] = (i, j)
                b_queens += 1
            if c == 'k':
                b_pieces[c] = (i, j)

    
    for w_type, w_position in w_pieces.items():
        #print(f"{w_type}: {w_position}")

        moves = get_moves(w_type, w_position, w_pieces, b_pieces)

        #print(sorted(moves))

        for m in moves:
            # Get new set of white pieces based on each possible move.
            #print(f"Moved {w_position} {m}")
            # Remember, pawns might get promoted.
            new_w_pieces = dict(w_pieces)
            # First pick piece up
            new_w_pieces.pop(w_type)
            # Check if the new piece was a pawn that got moved to the end
            # If so promote it to both Queen and Knight
            if w_type[0] == 'P' and m[0] == 0:
                new_w_pieces['Q99'] = m
                new_w_pieces['N99'] = m
            else:
                new_w_pieces[w_type] = m

            # Also need to account for attacks and pieces getting removed.
            # Account for capture
            new_b_pieces = dict(b_pieces)
            for b_type, b_pos in b_pieces.items():
                if b_pos == m:
                    new_b_pieces.pop(b_type)


            # Can't make a move that lets black mate you
            #print("Check if black mates white")
            if a_mates_b(new_b_pieces, new_w_pieces):
                continue
            # But want to find a move that mates black
            #print("Checking if white mates black")
            if a_mates_b(new_w_pieces, new_b_pieces):
                # print(f"{w_position} {m}")
                print(f"{f(w_position)}{f(m)}")
