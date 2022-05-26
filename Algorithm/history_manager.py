import json
from operator import contains
import re


class HistoryManager():
    def __init__(self, input):
        with open('./initBoard.json') as f:
           self.data = json.load(f)

        self.new_waste = input["waste-pile"]
        self.new_rows = input["row-stack"]

        self.init_stock = self.data['stock-pile']
        self.init_waste = self.data['waste-pile']
        self.init_suit = self.data['suit-stack']
        self.init_rows = self.data['row-stack']

        self.init_waste = self.new_waste ##init waste pile
        for i in range(len(self.init_rows)): ##init rows
            self.init_rows[f'row-{i+1}'][0] = self.new_rows[f'row-{i+1}']

        self.board = {
            "stock-pile": self.init_stock,
            "waste-pile": self.init_waste,
            "suit-stack": self.init_suit,
            "row-stack": self.init_rows
        }

        with open('board.json', 'w') as h:
            json.dump(self.board, h)            

    ##Find where unknown card is.
    ##Change to new input
    def update_board(self, new_input):
        ##Check if new input is from strategy manager, or from image rec
        if 'suit-stack' in new_input:
            self.board = new_input
        else: ##In suit stack is not in new input, new input is from image rec. 
            unknown_found = False
            ##Search for unknown card and stop when found
            while unknown_found == False:
                ##check if waste-pile has changed
                if self.board['waste-pile'] != new_input['waste-pile']:
                    self.board['waste-pile'] = new_input['waste-pile']
                    unknown_found = True
                ## Else run through the row stack, untill the new card is found. 
                else:
                    for row in self.board['row-stack']:
                        if self.board['row-stack'][row][0] == -1:
                            self.board['row-stack'][row][0] = new_input['row-stack'][row]
                            unknown_found = True

        with open('board.json', 'w') as h:
            json.dump(self.board, h)

    
    ##Check for victory

        
        


    