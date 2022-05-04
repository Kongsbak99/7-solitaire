from Algorithm.cards import Cards
import json

output = [
    {
        "hejsa": "hsahdas",

    }
]

usyduhsd = output[0]["hejsa"]

def movablePositions():
    legal_moves = []

    stockpile_card = MoveManager.board["waste-pile"][0]
    row1_topcard = MoveManager.board["row-stack"]["row-1"][0]
    row2_topcard = MoveManager.board["row-stack"]["row-2"][0]
    row3_topcard = MoveManager.board["row-stack"]["row-3"][0]
    row4_topcard = MoveManager.board["row-stack"]["row-4"][0]
    row5_topcard = MoveManager.board["row-stack"]["row-5"][0]
    row6_topcard = MoveManager.board["row-stack"]["row-6"][0]
    row7_topcard = MoveManager.board["row-stack"]["row-7"][0]

    cards = [row1_topcard, row2_topcard, row3_topcard, row4_topcard, row5_topcard, row6_topcard, row7_topcard]

    # Check whether any card can be moved on any of the other ones
    for top_card_looking in cards:
        # Check movables in row stacks
        for top_card_looked in cards:
            if MoveManager.canOverlay(top_card_looking, top_card_looked):
                move_message = Cards.getCardName(top_card_looking) + " can be moved on top of " + Cards.getCardName(top_card_looked)
                legal_moves.append(move_message)

        # Check movables of stock-pile card
        if MoveManager.canOverlay(stockpile_card, top_card_looking):
            move_message = Cards.getCardName(stockpile_card) + " can be moved on top of " + Cards.getCardName(top_card_looking)
            legal_moves.append(move_message)

        # Check movables in row stacks
        if MoveManager.canSuitStacked(top_card_looking) is not None:
            legal_moves.append(MoveManager.canSuitStacked(top_card_looking))

    if MoveManager.canSuitStacked(stockpile_card) is not None:
        legal_moves.append(MoveManager.canSuitStacked(stockpile_card))

    for message in legal_moves:
        print(message)


class MoveManager:
    board = {}
    with open('./boardHistory.json') as f:
        board = json.load(f)

    def __init__(self):
        pass

    # Check whether 1st card can be put on top of 2nd card (E.g. Ace of Spades on Two of Hearts)
    def canOverlay(card_id_1, card_id_2):
        card_1_value = Cards.getCardValue(card_id_1)
        card_1_suit = Cards.getCardSuit(card_id_1)

        card_2_value = Cards.getCardValue(card_id_2)
        card_2_suit = Cards.getCardSuit(card_id_2)

        if card_1_value == card_2_value - 1:
            if (card_1_suit == 1 or card_1_suit == 2) and (card_2_suit == 3 or card_2_suit == 4):
                return True
            elif (card_1_suit == 3 or card_1_suit == 4) and (card_2_suit == 1 or card_2_suit == 2):
                return True
        else:
            return False

    # Can the card be moved to a suit stack?
    def canSuitStacked(card_id):
        stack1_topcard = MoveManager.board["suit-stack"]["suit-1"][0]
        stack2_topcard = MoveManager.board["suit-stack"]["suit-2"][0]
        stack3_topcard = MoveManager.board["suit-stack"]["suit-3"][0]
        stack4_topcard = MoveManager.board["suit-stack"]["suit-4"][0]

        if ((card_id == stack1_topcard + 1) and (card_id >= 1) and (card_id <= 13)) or ((card_id == 1) and (stack1_topcard == 0)):
            return Cards.getCardName(card_id) + " can be moved to suit stack 1 (spades)"
        elif ((card_id == stack2_topcard + 1) and (card_id >= 14) and (card_id <= 26)) or ((card_id == 14) and (stack2_topcard == 0)):
            return Cards.getCardName(card_id) + " can be moved to suit stack 2 (clubs)"
        elif ((card_id == stack3_topcard + 1) and (card_id >= 27) and (card_id <= 39)) or ((card_id == 27) and (stack3_topcard == 0)):
            return Cards.getCardName(card_id) + " can be moved to suit stack 3 (heats)"
        elif ((card_id == stack4_topcard + 1) and (card_id >= 40) and (card_id <= 52)) or ((card_id == 40) and (stack4_topcard == 0)):
            return Cards.getCardName(card_id) + " can be moved to suit stack 4 (diamonds)"
        #else:
            return "Cannot be moved to any suit stacks"







