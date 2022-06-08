# New class to handle different types of moves as to not overpopulate move_manager

### MoveType: 6 ###

def kingWastepileToEmptyRow(move, board):
    row = board["row-stack"][move["to"]]
    card = move["cards"][0]

    # Add the card to the empty row
    row.append(card)

    # Find original row of card
    if card in board["row-stack"]["row-1"]:
        original_row = "row-1"
    elif card in board["row-stack"]["row-2"]:
        original_row = "row-2"
    elif card in board["row-stack"]["row-3"]:
        original_row = "row-3"
    elif card in board["row-stack"]["row-4"]:
        original_row = "row-4"
    elif card in board["row-stack"]["row-5"]:
        original_row = "row-5"
    elif card in board["row-stack"]["row-6"]:
        original_row = "row-6"
    elif card in board["row-stack"]["row-7"]:
        original_row = "row-7"
    else:
        print("ERROR - Cannot find row for card with ID: " + str(card))

    # Remove the card from the row
    board["row-stack"][original_row].remove(card)

    return board
