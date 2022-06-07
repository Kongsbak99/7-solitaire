# New class to handle different types of moves as to not overpopulate move_manager

def turnStockpile(board):
    wastepile = board["waste-pile"]
    stockpile = board["stock-pile"]
    output = []
    # If more than 3 cards in stockpile: turn three cards no problem
    if len(stockpile) >= 3:
        # Put top stockpile card as first element in waste pile
        wastepile.insert(0, stockpile.pop(0))
        wastepile.insert(0, stockpile.pop(0))
        wastepile.insert(0, stockpile.pop(0))

        # Make new top card next_input if unknown
        if wastepile[0] == 0:
            wastepile[0] = -1

    # If less than 3 cards, turn waste pile and put under stockpile
    # Stockpile will need to be turned over again
    elif len(stockpile) < 3:
        # Don't allow additional turns if stockpile is empty
        # and wastepile contains 3 or fewer cards
        if len(stockpile) == 0 and len(wastepile) <= 3:
            # Return output = input
            output = [stockpile, wastepile]
            # To get here, no more moves are possible
            print("No more available turnovers")

        else:
            # Turn waste pile by reversing order
            wastepile.reverse()
            # Put under (later in list) by appending individual cards to stockpile
            for card in wastepile:
                stockpile.append(card)
            # Empty waste pile
            wastepile = []

    board["waste-pile"] = wastepile
    board["stock-pile"] = stockpile
    return board
