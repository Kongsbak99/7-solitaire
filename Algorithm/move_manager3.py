from Algorithm.cards import Cards
import json


class MoveManager:
    legal_moves = []

    board = {}
    with open('./boardHistory.json') as f:
        board = json.load(f)

    def __init__(self):
        pass

    # Function to create JSON object of moves and add them to the list
    def createMoveObject(card_ids, move_location):
        move = {
            "moveId": int((len(MoveManager.legal_moves) + 1)),
            "cards": card_ids,
            "to": move_location
        }
        MoveManager.legal_moves.append(move)

    # Check whether 1st card can be put on top of 2nd card in the rows (E.g. Ace of Spaces on Two of Hearts)
    def canOverlay(card_id_1, card_id_2):
        card_1_value = Cards.getCardValue(card_id_1)
        card_1_suit = Cards.getCardSuit(card_id_1)

        card_2_value = Cards.getCardValue(card_id_2)
        card_2_suit = Cards.getCardSuit(card_id_2)

        # Card has to be 1 lower...
        # Verify a row's top card isn't ID: 0
        if card_2_value:
            if card_1_value == card_2_value - 1:
                # ...and of opposite color
                if (card_1_suit == 1 or card_1_suit == 2) and (card_2_suit == 3 or card_2_suit == 4):
                    return True
                elif (card_1_suit == 3 or card_1_suit == 4) and (card_2_suit == 1 or card_2_suit == 2):
                    return True
            else:
                return False

    # Return which suit stack a card is in
    def getSuitStack(card_id):
        result = ""
        if card_id == MoveManager.board["row-stack"]["row-1"][0]:
            result = "row-1"
        elif card_id == MoveManager.board["row-stack"]["row-2"][0]:
            result = "row-2"
        elif card_id == MoveManager.board["row-stack"]["row-3"][0]:
            result = "row-3"
        elif card_id == MoveManager.board["row-stack"]["row-4"][0]:
            result = "row-4"
        elif card_id == MoveManager.board["row-stack"]["row-5"][0]:
            result = "row-5"
        elif card_id == MoveManager.board["row-stack"]["row-6"][0]:
            result = "row-6"
        elif card_id == MoveManager.board["row-stack"]["row-7"][0]:
            result = "row-7"
        else:
            print("Whoops. Check function getSuitStack()")
        return result

    # Check whether a card can be moved to one of the four suit stacks and create their JSON move object
    def canSuitStacked(card_id):
        stack1 = MoveManager.board["suit-stack"]["suit-1"]
        stack2 = MoveManager.board["suit-stack"]["suit-2"]
        stack3 = MoveManager.board["suit-stack"]["suit-3"]
        stack4 = MoveManager.board["suit-stack"]["suit-4"]

        # Extra check since list can be empty
        if not stack1 and card_id == 1:
            MoveManager.createMoveObject([card_id], "suit-1")
        elif stack1:
            if ((card_id == stack1[0] + 1) and (card_id >= 1) and (card_id <= 13)):
                MoveManager.createMoveObject([card_id], "suit-1")

        if not stack2 and card_id == 14:
            MoveManager.createMoveObject([card_id], "suit-2")
        elif stack2:
            if ((card_id == stack2[0] + 1) and (card_id >= 14) and (card_id <= 26)):
                MoveManager.createMoveObject([card_id], "suit-2")

        if not stack2 and card_id == 27:
            MoveManager.createMoveObject([card_id], "suit-3")
        elif stack3:
            if ((card_id == stack3[0] + 1) and (card_id >= 27) and (card_id <= 39)):
                MoveManager.createMoveObject([card_id], "suit-3")

        if not stack4 and card_id == 40:
            MoveManager.createMoveObject([card_id], "suit-4")
        elif stack4:
            if ((card_id == stack4[0] + 1) and (card_id >= 40) and (card_id <= 52)):
                MoveManager.createMoveObject([card_id], "suit-4")


    # Create JSON for all possible moves
    def movables():
        movable_sets = []
        sets_topcard = []
        print("movable_sets: " + str(movable_sets))

        wastepile_card1 = MoveManager.board["waste-pile"][0]
        row1_topcard = MoveManager.board["row-stack"]["row-1"][0]
        row2_topcard = MoveManager.board["row-stack"]["row-2"][0]
        row3_topcard = MoveManager.board["row-stack"]["row-3"][0]
        row4_topcard = MoveManager.board["row-stack"]["row-4"][0]
        row5_topcard = MoveManager.board["row-stack"]["row-5"][0]
        row6_topcard = MoveManager.board["row-stack"]["row-6"][0]
        row7_topcard = MoveManager.board["row-stack"]["row-7"][0]
        cards = [row1_topcard, row2_topcard, row3_topcard, row4_topcard, row5_topcard, row6_topcard, row7_topcard]

        row1 = MoveManager.board["row-stack"]["row-1"]
        row2 = MoveManager.board["row-stack"]["row-2"]
        row3 = MoveManager.board["row-stack"]["row-3"]
        row4 = MoveManager.board["row-stack"]["row-4"]
        row5 = MoveManager.board["row-stack"]["row-5"]
        row6 = MoveManager.board["row-stack"]["row-6"]
        row7 = MoveManager.board["row-stack"]["row-7"]
        rows = [row1, row2, row3, row4, row5, row6, row7]

        # As cards only can have been moved to another row if they fit on top, we
        # know that all visible cards fit, and can be moved together as a set.
        # There for now extra check is required. Would also be difficult on JSON-objects without functions
        for row in rows:
            card_set = []
            for card in row:
                if card != 0:
                    card_set.append(card)
                    topcard = card
            movable_sets.append(card_set)
            if row[0] != 0:
                sets_topcard.append(topcard)

        print("movable_sets: " + str(movable_sets))
        print("sets_topcard: " + str(sets_topcard))

        # Check whether any card can be moved on any of the other ones
        for top_card_looking in sets_topcard:
            # Check movables in row stacks
            for top_card_looked in cards:
                if MoveManager.canOverlay(top_card_looking, top_card_looked):
                    MoveManager.createMoveObject([top_card_looking], MoveManager.getSuitStack(top_card_looked))

            # Check movables of waste-pile card moved to rows
            if MoveManager.canOverlay(wastepile_card1, top_card_looking):
                MoveManager.createMoveObject([wastepile_card1], MoveManager.getSuitStack(top_card_looking))

            # Check movables of row cards to suit stack
            MoveManager.canSuitStacked(top_card_looking)

        # Check movables of waste pile card to suit stack
        MoveManager.canSuitStacked(wastepile_card1)
