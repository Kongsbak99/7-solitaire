# New class to handle different types of moves as to not overpopulate move_manager

def wastepileToSuitStack(move, board):
    card = move["cards"][0]
    stack = move["to"]

    # Append card to suit stack
    board["suit-stack"][stack].append[card]

    # Remove card from waste pile
    board["waste-pile"].remove(card)

    # Make new top card next_input if unknown
    if board["waste-pile"][0] == 0:
        board["waste-pile"][0] = -1

    return board
