from Algorithm.cards import Cards
import json


# New class to handle different types of moves as to not overpopulate move_manager

def turnStockpile(stockpile, wastepile):
    output = []
    # If 3 or more cards in stock-pile: turn three cards no problem
    if len(stockpile) >= 3:
        # Put top stockpile card as first element in wastepile
        wastepile.insert(0, stockpile.pop(0))
        wastepile.insert(0, stockpile.pop(0))
        wastepile.insert(0, stockpile.pop(0))
        output = [stockpile, wastepile]

    # If less than 3 three cards, turn wastepile and put under stockpile
    elif len(stockpile) < 3:
        # Turn wastepile by reversing order
        wastepile.reverse()
        # Put under (later in list) by appending individual cards to stockpile
        for card in wastepile:
            stockpile.append(card)
        wastepile = []
        output = [stockpile, wastepile]

    return output
