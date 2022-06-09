# New class to handle different types of moves as to not overpopulate move_manager

### MoveType: 4 ###

def rowToSuitstack(move, board):
    card = move["cards"][0]
    suit_stack = move["to"]

    # Add the card to the suit stack
    board["suit-stack"][suit_stack].append(card)

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

    # Make top leftover card visible if not
    # But only if there are cards left
    if board["row-stack"][original_row]:
        if board["row-stack"][original_row][0] == 0:
            board["row-stack"][original_row][0] = -1

    return board
