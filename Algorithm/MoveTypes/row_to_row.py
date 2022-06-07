# New class to handle different types of moves as to not overpopulate move_manager

def rowToRow(move, board):
    cards = move["cards"]
    row = board["row-stack"][move["to"]]

    # Cards should be individually added to the row to avoid a nested list
    # Therefore, the card order should first be reversed
    cards_reversed = list(reversed(cards))

    for card in cards_reversed:
        # Remove card from actual row
        if card in board["row-stack"]["row-1"]:
            board["row-stack"]["row-1"].remove(card)
        elif card in board["row-stack"]["row-2"]:
            board["row-stack"]["row-2"].remove(card)
        elif card in board["row-stack"]["row-3"]:
            board["row-stack"]["row-3"].remove(card)
        elif card in board["row-stack"]["row-4"]:
            board["row-stack"]["row-4"].remove(card)
        elif card in board["row-stack"]["row-5"]:
            board["row-stack"]["row-5"].remove(card)
        elif card in board["row-stack"]["row-6"]:
            board["row-stack"]["row-6"].remove(card)
        elif card in board["row-stack"]["row-7"]:
            board["row-stack"]["row-7"].remove(card)
        else:
            print("ERROR - Cannot find row for card with ID: " + str(card))

    # Then add the cards one-by-one
    for card in cards_reversed:
        row.insert(0, card)

    return board
