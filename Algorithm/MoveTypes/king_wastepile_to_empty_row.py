# New class to handle different types of moves as to not overpopulate move_manager

### MoveType: 6 ###

def kingWastepileToEmptyRow(move, board):
    row = board["row-stack"][move["to"]]
    card = move["cards"][0]

    # Add the card to the empty row
    row.append(card)

    # Remove the card from the wastepile
    board["waste-pile"].remove(card)

    # Make new top card next_input if unknown
    # But only if there are cards left
    if board["waste-pile"]:
        if board["waste-pile"][0] == 0:
            board["waste-pile"][0] = -1

    return board
