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
    def getRow(card_id):
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

        # Extra check since list should be empty at first
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

        row_topcards = []
        rows = []
        if MoveManager.board["row-stack"]["row-1"]:
            rows.append(MoveManager.board["row-stack"]["row-1"])
            row_topcards.append(MoveManager.board["row-stack"]["row-1"][0])
        if MoveManager.board["row-stack"]["row-2"]:
            rows.append(MoveManager.board["row-stack"]["row-2"])
            row_topcards.append(MoveManager.board["row-stack"]["row-2"][0])
        if MoveManager.board["row-stack"]["row-3"]:
            rows.append(MoveManager.board["row-stack"]["row-3"])
            row_topcards.append(MoveManager.board["row-stack"]["row-3"][0])
        if MoveManager.board["row-stack"]["row-4"]:
            rows.append(MoveManager.board["row-stack"]["row-4"])
            row_topcards.append(MoveManager.board["row-stack"]["row-4"][0])
        if MoveManager.board["row-stack"]["row-5"]:
            rows.append(MoveManager.board["row-stack"]["row-5"])
            row_topcards.append(MoveManager.board["row-stack"]["row-5"][0])
        if MoveManager.board["row-stack"]["row-6"]:
            rows.append(MoveManager.board["row-stack"]["row-6"])
            row_topcards.append(MoveManager.board["row-stack"]["row-6"][0])
        if MoveManager.board["row-stack"]["row-7"]:
            rows.append(MoveManager.board["row-stack"]["row-7"])
            row_topcards.append(MoveManager.board["row-stack"]["row-7"][0])

        if MoveManager.board["waste-pile"]:
            wastepile_card1 = MoveManager.board["waste-pile"][0]


        for row in rows:
            temp_set = []
            for card in row:
                if card > 0:
                    temp_set.append(card)
                    movable_sets.append(temp_set[:])


        # Check whether any movable_sets can be moved to any of the other row's top card
        for card_set in movable_sets:
            check_card = card_set[len(card_set)-1]
            for topcard in row_topcards:
                if MoveManager.canOverlay(check_card, topcard):
                    MoveManager.createMoveObject(card_set, MoveManager.getRow(topcard))

        # Check whether the top waste-pile card can be moved to a row
        # And if a row top-card can be moved to its suit stack
        for topcard in row_topcards:
            if MoveManager.canOverlay(wastepile_card1, topcard):
                MoveManager.createMoveObject([wastepile_card1], MoveManager.getRow(topcard))
            MoveManager.canSuitStacked(topcard)

        # Check movables of waste pile card to suit stack
        MoveManager.canSuitStacked(wastepile_card1)
