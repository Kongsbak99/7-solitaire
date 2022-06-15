import json
from operator import contains
import re

from Algorithm.PlayLoopFunctions.image_rec_confirmer import confirmCard
from Algorithm.PlayLoopFunctions.mock_input import imgrec_service, mock, mockImageRec

from Algorithm.cards import Cards
from ImageRecognition.run import runAllCards


class HistoryManager():
    def __init__(self, input):
        with open('./initBoard.json') as f:
           self.data = json.load(f)

        ## init input from image rec
        self.new_waste = input["waste-pile"]
        self.new_rows = input["row-stack"]

        ## init board from initBoard.json (empty board only with unknowns) 
        self.init_stock = self.data['stock-pile']
        self.init_waste = self.data['waste-pile']
        self.init_suit = self.data['suit-stack']
        self.init_rows = self.data['row-stack']
        
        rec_card = self.new_waste[0]
        actual_waste = confirmCard(rec_card)
        self.init_waste[0] = actual_waste ##init waste pile
        for i in range(len(self.init_rows)): ##init rows
            rec_card = self.new_rows[f'row-{i+1}']
            actual_card = confirmCard(rec_card)
            self.init_rows[f'row-{i+1}'][0] = actual_card

        self.board = {
            "stock-pile": self.init_stock,
            "waste-pile": self.init_waste,
            "suit-stack": self.init_suit,
            "row-stack": self.init_rows
        }

        ## Save starting board
        with open('board.json', 'w') as h:
            json.dump(self.board, h)            

    

    ##Find where unknown card is.
    ##Change to new input
    def update_board(self, board):
        if board['waste-pile']:
            if board['waste-pile'][0] == -1:
                imgrec_input = runAllCards() # TODO i stedet for mock(), deres metode
                imgrec_to_json = imgrec_service(imgrec_input)
                #TODO Fjern linje:
                rec_card = mockImageRec() 
                #TODO fjern hashtag: 
                #rec_card = imgrec_to_json['row-stack'][row]
                rec_card = mockImageRec() 
                actual_card = confirmCard(rec_card)
                board['waste-pile'][0] = actual_card
        for row in board['row-stack']:
            if board["row-stack"][row]:
                if board['row-stack'][row][0] == -1:
                    imgrec_input = runAllCards() # TODO i stedet for mock(), deres metode
                    imgrec_to_json = imgrec_service(imgrec_input)
                    #TODO Fjern:
                    rec_card = mockImageRec()
                    #TODO fjern hashtag:
                    #rec_card = imgrec_to_json['row-stack'][row]
                    actual_card = confirmCard(rec_card)
                    board['row-stack'][row][0] = actual_card
        
        self.board = board
        with open('board.json', 'w') as h:
            json.dump(self.board, h)
        
        return self.board

    
    ##Check for victory
    def check_for_victory(self):
        with open('./board.json') as f:
           self.board = json.load(f)
        suit1_top = self.board['suit-stack']['suit-1'][len(self.board['suit-stack']['suit-1']) - 1]
        suit2_top = self.board['suit-stack']['suit-2'][len(self.board['suit-stack']['suit-2']) - 1]
        suit3_top = self.board['suit-stack']['suit-3'][len(self.board['suit-stack']['suit-3']) - 1]
        suit4_top = self.board['suit-stack']['suit-4'][len(self.board['suit-stack']['suit-4']) - 1]
        # Check if top card of each stack is the final card.
        if suit1_top == 13 and suit2_top == 26 and suit3_top == 39 and suit4_top == 52:
            return True
        else: return False

        
        


    