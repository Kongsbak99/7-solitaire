import json

# New class to handle different types of moves as to not overpopulate move_manager

### MoveType: 3 ###

def rowToRow_new(move, board):
    cards = move["cards"]
    row = board["row-stack"][move["to"]]

    cards_reversed = list(reversed(cards))

    row1 = board["row-stack"]["row-1"]
    row2 = board["row-stack"]["row-2"]
    row3 = board["row-stack"]["row-3"]
    row4 = board["row-stack"]["row-4"]
    row5 = board["row-stack"]["row-5"]
    row6 = board["row-stack"]["row-6"]
    row7 = board["row-stack"]["row-7"]

    # Orignal cards
    if cards[0] in row1:
        original_row = row1
        string = "row-1"
    elif cards[0] in row2:
        original_row = row2
        string = "row-2"
    elif cards[0] in row3:
        original_row = row3
        string = "row-3"
    elif cards[0] in row4:
        original_row = row4
        string = "row-4"
    elif cards[0] in row5:
        original_row = row5
        string = "row-5"
    elif cards[0] in row6:
        original_row = row6
        string = "row-6"
    elif cards[0] in row7:
        original_row = row7
        string = "row-7"
    else:
        print("Dummernik!")

    # Remove the cards from the original row
    for card in cards_reversed:
        original_row.remove(card)

    if original_row:
        if original_row[0] == 0:
            original_row = -1

    for card in cards_reversed:
        row.insert(0, card)

    board["row-stack"][string] = original_row
    board["row-stack"][move["to"]] = row
    return board

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
    # But only if there are cards left
    if board["row-stack"][original_row]:
        if board["row-stack"][original_row][0] == 0:
            board["row-stack"][original_row][0] = -1


    # Then add the cards one-by-one to the new row
    for card in cards_reversed:
        row.insert(0, card)

    # print("R2R: " + str(board))
    return board
