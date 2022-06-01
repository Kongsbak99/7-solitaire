from hashlib import new
from Algorithm.cards import Cards
import json


class MoveManager:
    def __init__(self):
        self.legal_moves = []

        with open('./board.json') as f:
            self.board = json.load(f)

    

    # Function to create JSON object of moves and add them to the list
    def createMoveObject(self, card_ids, move_location):
        move = {
            "moveId": int((len(self.legal_moves) + 1)),
            "cards": card_ids,
            "to": move_location
        }
        self.legal_moves.append(move)

    # Check whether 1st card can be put on top of 2nd card in the rows (E.g. Ace of Spaces on Two of Hearts)
    def canOverlay(self, card_id_1, card_id_2):
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
    def getSuitStack(self, card_id):
        result = ""
        if card_id == self.board["row-stack"]["row-1"][0]:
            result = "row-1"
        elif card_id == self.board["row-stack"]["row-2"][0]:
            result = "row-2"
        elif card_id == self.board["row-stack"]["row-3"][0]:
            result = "row-3"
        elif card_id == self.board["row-stack"]["row-4"][0]:
            result = "row-4"
        elif card_id == self.board["row-stack"]["row-5"][0]:
            result = "row-5"
        elif card_id == self.board["row-stack"]["row-6"][0]:
            result = "row-6"
        elif card_id == self.board["row-stack"]["row-7"][0]:
            result = "row-7"
        else:
            print("Whoops. Check function getSuitStack()")
        return result

    # Check whether a card can be moved to one of the four suit stacks and create their JSON move object
    def canSuitStacked(self, card_id):
        stack1 = self.board["suit-stack"]["suit-1"]
        stack2 = self.board["suit-stack"]["suit-2"]
        stack3 = self.board["suit-stack"]["suit-3"]
        stack4 = self.board["suit-stack"]["suit-4"]

        # Extra check since list can be empty
        if not stack1 and card_id == 1:
            self.createMoveObject([card_id], "suit-1")
        elif stack1:
            if ((card_id == stack1[len(stack1)-1] + 1) and (card_id >= 1) and (card_id <= 13)):
                self.createMoveObject([card_id], "suit-1")
            elif card_id == 1 and len(stack1) <= 1:
                self.createMoveObject([card_id], "suit-1")

        if not stack2 and card_id == 14:
            self.createMoveObject([card_id], "suit-2")
        elif stack2:
            if ((card_id == stack2[len(stack2)-1] + 1) and (card_id >= 14) and (card_id <= 26)):
                self.createMoveObject([card_id], "suit-2")
            elif card_id == 14 and len(stack2) <= 1:
                self.createMoveObject([card_id], "suit-2")

        if not stack2 and card_id == 27:
            self.createMoveObject([card_id], "suit-3")
        elif stack3:
            if ((card_id == stack3[len(stack3)-1] + 1) and (card_id >= 27) and (card_id <= 39)):
                self.createMoveObject([card_id], "suit-3")
            elif card_id == 27 and len(stack3) <= 1:
                self.createMoveObject([card_id], "suit-3")

        if not stack4 and card_id == 40:
            self.createMoveObject([card_id], "suit-4")
        elif stack4:
            if ((card_id == stack4[len(stack2)-1] + 1) and (card_id >= 40) and (card_id <= 52)):
                self.createMoveObject([card_id], "suit-4")
            elif card_id == 40 and len(stack4) <= 1:
                self.createMoveObject([card_id], "suit-4")

    # Create JSON for all possible moves
    def movables(self):
        with open('./board.json') as f:
            board = json.load(f)

        wastepile_card1 = board["waste-pile"][0]
        wastepile_card2 = board["waste-pile"][1]
        wastepile_card3 = board["waste-pile"][2]
        row1_topcard = board["row-stack"]["row-1"][0]
        row2_topcard = board["row-stack"]["row-2"][0]
        row3_topcard = board["row-stack"]["row-3"][0]
        row4_topcard = board["row-stack"]["row-4"][0]
        row5_topcard = board["row-stack"]["row-5"][0]
        row6_topcard = board["row-stack"]["row-6"][0]
        row7_topcard = board["row-stack"]["row-7"][0]

        cards = [row1_topcard, row2_topcard, row3_topcard, row4_topcard, row5_topcard, row6_topcard, row7_topcard]

        waste_pile_cards = [wastepile_card1, wastepile_card2, wastepile_card3]

        # Check whether any card can be moved on any of the other ones
        for top_card_looking in cards:
            # Check movables in row stacks
            for top_card_looked in cards:
                if self.canOverlay(top_card_looking, top_card_looked):
                    self.createMoveObject([top_card_looking], self.getSuitStack(top_card_looked))

            # Check movables of waste-pile
            for card in waste_pile_cards:
                # heck movables for waste pile card moved to row
                if self.canOverlay(card, top_card_looking):
                    self.createMoveObject([wastepile_card1], self.getSuitStack(top_card_looking))
            

            # Check movables of row cards to suit stack
            self.canSuitStacked(top_card_looking)

        for card in waste_pile_cards:
            # Check movables of waste pile card to suit stack
            self.canSuitStacked(card)


    def make_move(self, move, board):
    
        try:
            ############ Check if no moves, turn new waste pile ############
            if len(move) == 0:
                board['deprecated-waste'].append(board['waste-pile'])
                board['waste-pile'] = [-1, -1, -1]
                board['stock-pile'].remove(0)
                board['stock-pile'].remove(0)
                board['stock-pile'].remove(0)
            ############ Cleanup old location of card(s) ############
            else:
                bottom_card = move['cards'][0]
                ##If moved from waste pile, simply just remove card from array
                for card in board['waste-pile']:
                    if card == bottom_card:
                        board['waste-pile'].remove(card)
                
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
                        #Update board with new row. 
                        board['row-stack'][row] = new_row

            ############ Then update new location of card(s) ############
                #Check if cards should be moved to suit stack
                for stack in board['suit-stack']:
                    if stack == move['to']:
                        for card in move['cards']:
                            board['suit-stack'][stack].append(card)
                
                ##Check if cards should be moved to row stack
                for row in board['row-stack']:
                    if row == move['to']:
                        #make new row in correct order
                        new_row = move['cards']
                        for card in board['row-stack'][row]:
                            new_row.append(card)
                        #Update board row. 
                        board['row-stack'][row] = new_row
                print(" ")
                print(f"made move: {move}")
                print(" ")
            
            self.board = board
            ############ Finally return the new board, with the move made and a potential new unknown card. ############
            return board
        except Exception as e:
            print(f"Failed to make move: {move}")
            print(f"Threw exception {e}")
     
