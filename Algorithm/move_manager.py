from Algorithm.cardss import Cardss
from Algorithm.MoveTypes.turn_stockpile import turnStockpile
from Algorithm.MoveTypes.wastepile_to_suitstack import wastepileToSuitStack
from Algorithm.MoveTypes.wastepile_to_row import wastepileToRow
from Algorithm.MoveTypes.row_to_row import rowToRow
from Algorithm.MoveTypes.row_to_suitstack import rowToSuitstack
from Algorithm.MoveTypes.king_row_to_empty_row import kingRowToEmptyRow
from Algorithm.MoveTypes.king_wastepile_to_empty_row import kingWastepileToEmptyRow
import json


class MoveManager:
    def __init__(self):
        self.legal_moves = []

        with open('board.json') as f:
            self.board = json.load(f)
            f.close()
        f.close()

    # Function to create JSON object of moves and add them to the list
    def createMoveObject(self, card_ids, move_location, moveType):
        move = {
            "moveId": int((len(self.legal_moves))),
            "cards": card_ids,
            "to": move_location,
            "moveType": moveType
        }
        self.legal_moves.append(move)

    # Check whether 1st card can be put on top of 2nd card in the rows (E.g. Ace of Spaces on Two of Hearts)
    def canOverlay(self, card_id_1, card_id_2):
        card_1_value = Cardss.getCardValue(card_id_1)
        card_1_suit = Cardss.getCardSuit(card_id_1)

        card_2_value = Cardss.getCardValue(card_id_2)
        card_2_suit = Cardss.getCardSuit(card_id_2)

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
    def getRow(self, card_id):
        result = ""
        if self.board["row-stack"]["row-1"]:
            if card_id == self.board["row-stack"]["row-1"][0]:
                result = "row-1"
        if self.board["row-stack"]["row-2"]:
            if card_id == self.board["row-stack"]["row-2"][0]:
                result = "row-2"
        if self.board["row-stack"]["row-3"]:
            if card_id == self.board["row-stack"]["row-3"][0]:
                result = "row-3"
        if self.board["row-stack"]["row-4"]:
            if card_id == self.board["row-stack"]["row-4"][0]:
                result = "row-4"
        if self.board["row-stack"]["row-5"]:
            if card_id == self.board["row-stack"]["row-5"][0]:
                result = "row-5"
        if self.board["row-stack"]["row-6"]:
            if card_id == self.board["row-stack"]["row-6"][0]:
                result = "row-6"
        if self.board["row-stack"]["row-7"]:
            if card_id == self.board["row-stack"]["row-7"][0]:
                result = "row-7"
        else:
            print("Whoops. Check function getSuitStack()")
        return result

    # Check whether a card can be moved to one of the four suit stacks and create their JSON move object
    def canSuitStacked(self, card_id, moveType):
        stack1 = self.board["suit-stack"]["suit-1"]
        stack2 = self.board["suit-stack"]["suit-2"]
        stack3 = self.board["suit-stack"]["suit-3"]
        stack4 = self.board["suit-stack"]["suit-4"]

        # Extra check since list should be empty at first
        if not stack1 and card_id == 1:
            self.createMoveObject([card_id], "suit-1", moveType)
        elif stack1:
            if ((card_id == stack1[len(stack1) - 1] + 1) and (card_id >= 1) and (card_id <= 13)):
                self.createMoveObject([card_id], "suit-1", moveType)
            elif card_id == 1 and len(stack1) <= 1:
                self.createMoveObject([card_id], "suit-1", moveType)
        if not stack2 and card_id == 14:
            self.createMoveObject([card_id], "suit-2", moveType)
        elif stack2:
            if ((card_id == stack2[len(stack2) - 1] + 1) and (card_id >= 14) and (card_id <= 26)):
                self.createMoveObject([card_id], "suit-2", moveType)
            elif card_id == 14 and len(stack2) <= 1:
                self.createMoveObject([card_id], "suit-2", moveType)

        if not stack3 and card_id == 27:
            self.createMoveObject([card_id], "suit-3", moveType)
        elif stack3:
            if ((card_id == stack3[len(stack3) - 1] + 1) and (card_id >= 27) and (card_id <= 39)):
                self.createMoveObject([card_id], "suit-3", moveType)
            elif card_id == 27 and len(stack3) <= 1:
                self.createMoveObject([card_id], "suit-3", moveType)

        if not stack4 and card_id == 40:
            self.createMoveObject([card_id], "suit-4", moveType)
        elif stack4:
            if ((card_id == stack4[len(stack4) - 1] + 1) and (card_id >= 40) and (card_id <= 52)):
                self.createMoveObject([card_id], "suit-4", moveType)
            elif card_id == 40 and len(stack4) <= 1:
                self.createMoveObject([card_id], "suit-4", moveType)

    # Create JSON for all possible moves
    def movables(self):
        movable_sets = []

        # Empty rows to know where kings can be moved
        empty_rows = []

        row_topcards = []
        rows = []
        if self.board["row-stack"]["row-1"]:
            rows.append(self.board["row-stack"]["row-1"])
            row_topcards.append(self.board["row-stack"]["row-1"][0])
        elif not self.board["row-stack"]["row-1"]:
            empty_rows.append("row-1")
        if self.board["row-stack"]["row-2"]:
            rows.append(self.board["row-stack"]["row-2"])
            row_topcards.append(self.board["row-stack"]["row-2"][0])
        elif not self.board["row-stack"]["row-2"]:
            empty_rows.append("row-2")
        if self.board["row-stack"]["row-3"]:
            rows.append(self.board["row-stack"]["row-3"])
            row_topcards.append(self.board["row-stack"]["row-3"][0])
        elif not self.board["row-stack"]["row-3"]:
            empty_rows.append("row-3")
        if self.board["row-stack"]["row-4"]:
            rows.append(self.board["row-stack"]["row-4"])
            row_topcards.append(self.board["row-stack"]["row-4"][0])
        elif not self.board["row-stack"]["row-4"]:
            empty_rows.append("row-4")
        if self.board["row-stack"]["row-5"]:
            rows.append(self.board["row-stack"]["row-5"])
            row_topcards.append(self.board["row-stack"]["row-5"][0])
        elif not self.board["row-stack"]["row-5"]:
            empty_rows.append("row-5")
        if self.board["row-stack"]["row-6"]:
            rows.append(self.board["row-stack"]["row-6"])
            row_topcards.append(self.board["row-stack"]["row-6"][0])
        elif not self.board["row-stack"]["row-6"]:
            empty_rows.append("row-6")
        if self.board["row-stack"]["row-7"]:
            rows.append(self.board["row-stack"]["row-7"])
            row_topcards.append(self.board["row-stack"]["row-7"][0])
        elif not self.board["row-stack"]["row-7"]:
            empty_rows.append("row-7")



        # waste_pile_cards = [self.board["waste-pile"][0], self.board["waste-pile"][1], self.board["waste-pile"][2]]

        for row in rows:
            temp_set = []
            for card in row:
                if card > 0:
                    temp_set.append(card)
                    movable_sets.append(temp_set[:])

        # Check whether any movable_sets can be moved to any of the other row's top card
        for card_set in movable_sets:
            check_card = card_set[len(card_set) - 1]
            for topcard in row_topcards:
                if self.canOverlay(check_card, topcard):
                    self.createMoveObject(card_set, self.getRow(topcard), 3)
            # Check if any of the sets are only kings, and if there's an empty row
            if (card_set == [13] or card_set == [26] or card_set == [39] or card_set == [52]) and empty_rows:
                for empty_row in empty_rows:
                    self.createMoveObject(card_set, empty_row, 5)


        # Check whether the top waste-pile card can be moved to a row

        for topcard in row_topcards:
            if self.board["waste-pile"]:
                wastepile_card1 = self.board["waste-pile"][0]
                if self.canOverlay(wastepile_card1, topcard):
                    self.createMoveObject([wastepile_card1], self.getRow(topcard), 2)
            # And if a row top-card can be moved to its suit stack
            self.canSuitStacked(topcard, 4)

        if self.board["waste-pile"]:
            wastepile_card1 = self.board["waste-pile"][0]
            # Also check for king in wastepile and an available empty row
            if (wastepile_card1 == 13 or wastepile_card1 == 26 or wastepile_card1 == 39 or wastepile_card1 == 52) \
                    and empty_rows:
                self.createMoveObject([wastepile_card1], empty_rows[0], 6)

            # Check movables of waste pile card to suit stack
            self.canSuitStacked(wastepile_card1, 1)


        # Force turnover as only move if stockpile + wastepile = 3 cards and they're not in wastepile
        if (len(self.board["stock-pile"]) + len(self.board["waste-pile"]) == 3) and len(self.board["waste-pile"]) < 3:
            self.legal_moves.clear()
        # Add turnover of stockpile as a move, but not if stockpile is empty and wastepile <= 3 cards
        if not (not bool(self.board["stock-pile"]) and len(self.board["waste-pile"]) <= 3):
            self.legal_moves.append({'moveId': int((len(self.legal_moves))), 'moveType': 7})

    def doMove(self, move):  # TODO
        if move["moveType"] == 1:
            board = wastepileToSuitStack(move, self.board)
        elif move["moveType"] == 2:
            board = wastepileToRow(move, self.board)
        elif move["moveType"] == 3:
            board = rowToRow(move, self.board)
        elif move["moveType"] == 4:
            board = rowToSuitstack(move, self.board)
        elif move["moveType"] == 5:
            board = kingRowToEmptyRow(move, self.board)
        elif move["moveType"] == 6:
            board = kingWastepileToEmptyRow(move, self.board)
        elif move["moveType"] == 7:
            board = turnStockpile(self.board)
        else:
            print("ERROR - Unknown moveType: " + str(move["moveType"]))
        #fil = open('board.json', 'w')
        #json.dump(board, fil)
        #print("MM1: " + str(board))
        #fil.close()
        #print("MM2: " + str(board))
        return board
       # with open('board.json', 'w') as h:
        #    json.dump(board, h)



    def make_move(self, move, board):

        try:
            ############ Check if no moves, turn new waste pile ############
            if len(move) == 0:
                # If more than 3 cards in stock-pile, turn three cards no problem
                if len(board["stock-pile"]) >= 3:
                    # Put top stock-pile card in waste-pile
                    board["waste-pile"].insert(0, board["stock-pile"].pop(0))
                    board["waste-pile"].insert(0, board["stock-pile"].pop(0))
                    board["waste-pile"].insert(0, board["stock-pile"].pop(0))

                if len(board["stock-pile"]) < 3:
                    print("Under 3 cards in stock pile")

                # board['deprecated-waste'].append(board['waste-pile'])
                # board['waste-pile'] = [-1, -1, -1]
                # board['stock-pile'].remove(0)
                # board['stock-pile'].remove(0)
                # board['stock-pile'].remove(0)

            else:
                ############ First cleanup old location of card(s) ############
                bottom_card = move['cards'][0]
                ##If moved from waste pile, simply just remove card from array
                for card in board['waste-pile']:
                    if card == bottom_card:
                        board['waste-pile'].remove(card)
                        board['waste-pile'].insert(0, -1)
                        

                ##If moved from row stack, create new row with potential unknown card.
                for row in board['row-stack']:
                    ##if card matches, cleanup row and make unknown (-1)
                    if board['row-stack'][row][0] == bottom_card:
                        new_row = []
                        for card in board['row-stack'][row]:
                            if card == 0:
                                new_row.append(card)
                        ##If bottom card is 0, then make that an unknown card (-1)
                        if new_row[0] == 0:
                            new_row[0] = -1
                        # Update board with new row.
                        board['row-stack'][row] = new_row

                ############ Then update new location of card(s) ############
                # Check if cards should be moved to suit stack
                for stack in board['suit-stack']:
                    if stack == move['to']:
                        for card in move['cards']:
                            board['suit-stack'][stack].append(card)

                ##Check if cards should be moved to row stack
                for row in board['row-stack']:
                    if row == move['to']:
                        # make new row in correct order
                        new_row = move['cards']
                        for card in board['row-stack'][row]:
                            new_row.append(card)
                        # Update board row.
                        board['row-stack'][row] = new_row

            ############ Finally return the new board, with the move made and a potential new unknown card. ############
            self.board = board
            return board

        except Exception as e:
            print(f"Failed to make move: {move}")
            print(f"Threw exception {e}")
