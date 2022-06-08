# New class to handle different types of moves as to not overpopulate move_manager

### MoveType: 2 ###

def wastepileToRow(move, board):
    card = move["cards"][0]
    row = board["row-stack"][move["to"]]

    # Insert card as row's first card
    row.insert(0, card)

    # Remove card from waste pile
    board["waste-pile"].remove(card)

    # Make new top card next_input if unknown
    # But only if there are cards left
    if board["waste-pile"]:
        if board["waste-pile"][0] == 0:
            board["waste-pile"][0] = -1

    return board
