# New class to handle different types of moves as to not overpopulate move_manager

### MoveType: 3 ###

def rowToRow(move, board):
    cards = move["cards"]
    row = board["row-stack"][move["to"]]

    # Cards should be individually added to the row to avoid a nested list
    # Therefore, the card order should first be reversed
    cards_reversed = list(reversed(cards))

    # Find original row of cards
    if cards[0] in board["row-stack"]["row-1"]:
        original_row = "row-1"
    elif cards[0] in board["row-stack"]["row-2"]:
        original_row = "row-2"
    elif cards[0] in board["row-stack"]["row-3"]:
        original_row = "row-3"
    elif cards[0] in board["row-stack"]["row-4"]:
        original_row = "row-4"
    elif cards[0] in board["row-stack"]["row-5"]:
        original_row = "row-5"
    elif cards[0] in board["row-stack"]["row-6"]:
        original_row = "row-6"
    elif cards[0] in board["row-stack"]["row-7"]:
        original_row = "row-7"
    else:
        print("ERROR - Cannot find row for card with ID: " + str(cards[0]))

    # Remove the cards from the original row
    for card in cards_reversed:
        board["row-stack"][original_row].remove(card)

    # Make top leftover card visible if not
    if board["row-stack"][original_row][0] == 0:
        board["row-stack"][original_row][0] = -1


    # Then add the cards one-by-one to the new row
    for card in cards_reversed:
        row.insert(0, card)

    return board
