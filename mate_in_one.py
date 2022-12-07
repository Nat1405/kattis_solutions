import sys



def get_moves(a_type, a_position, a_pieces, b_pieces):
    '''a_pieces are attackers, b_pieces are defenders.'''
    moves = []
    if a_type[0].lower() in {'k', 'q', 'b', 'r'}:
        # These pieces move linearly to some extent.
        moves.extend(
            linear_move_checker(
                a_type.lower(),
                a_position,
                a_pieces,
                b_pieces
            )
        )
    else:
        raise NotImplementedError()

    return moves


def linear_move_checker(*args):
    '''Might be more efficient ways that take more code'''
    moves = []

    # Branch out radially from piece
    ranges = [(8,1,1,1), (-8,-1,1,1), (1,1,8,1), (1,1,-8,-1)]

    for r in ranges:
        moves.extend(check_linear_direction(r, *args))

    return moves


def check_linear_direction(r, p_type, p_pos, a_pieces, b_pieces):
    '''Checks a single linear direction'''
    moves = []
    u,v,x,y = r
    for i in range(0, u, v):
        for j in range(0, x, y):
            # Short-circuit conditions here to skip invalid
            # move positions. There are probably more efficient
            # ways to check moves, but I'm not gunning for the
            # worlds fastest chest engine.
            if i == 0 and j == 0:
                continue # Can't move to same position
            elif p_type == 'r':
                if i != j:
                    continue # Rooks
            elif p_type == 'b':
                if i != 0 and j != 0:
                    continue # Bishops
            elif p_type == 'k':
                if abs(i) > 1 or abs(j) > 1:
                    continue # Kings
            elif p_type == 'q':
                print(f"{i} {j}")
                # if (i==j) or (i==0 and j!=0) or (i!=0 and j==0):
                #     print(f"EQUALS {i} {j}")
                # else:
                #     print(f"{i} {j}")
                #     continue

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
            # if new_pos in a_pieces.values():
            #     return moves
            
            # # If hit an opponent, take the move and stop extending.
            # if new_pos in b_pieces.values():
            #     moves.append(new_pos)
            #     return moves
            
            # moves.append(new_pos)
    
    return moves




if __name__ == "__main__":
    w_pieces = {}
    b_pieces = {}
    
    # Need unique keys for each piece
    w_pawns = 0
    w_rooks = 0
    w_bishops = 0
    w_knights = 0
    b_pawns = 0
    b_rooks = 0
    b_bishops = 0
    b_knights = 0

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
                w_pieces[c] = (i, j)
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
                b_pieces[c] = (i, j)
            if c == 'k':
                b_pieces[c] = (i, j)

    # for e in sorted(w_pieces.items()):
    #     print(e)

    # print()

    # for e in sorted(b_pieces.items()):
    #     print(e)

    
    for w_type, w_position in w_pieces.items():
        print(f"{w_type}: {w_position}")

        if w_type[0] in {'P', 'N'}:
            print(f"Skipping {w_type[0]}")
            continue

        moves = get_moves(w_type, w_position, w_pieces, b_pieces)

        print(moves)      

