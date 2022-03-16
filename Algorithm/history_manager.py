import json
from operator import contains
import re


class HistoryManager():
    def __init__(self, id):
        #with open('./board.json') as f:
        #   self.data = json.load(f)

        #with open('boardHistory.json', 'w') as h:
        #    json.dump(self.data, h)
        self.id = id


    def check_history(self):
        with open('./board.json') as f:
           self.data = json.load(f)

        with open('./boardHistory.json') as f:
           self.history = json.load(f)

        self.stock_pile = self.data['stock-pile']
        self.waste_pile = self.data['waste-pile']
        self.suit_stack = self.data['suit-stack']
        self.row_stack = self.data['row-stack']

        self.historic_stock_pile = self.history['stock-pile']
        self.historic_waste_pile = self.history['waste-pile']
        self.historic_suit_stack = self.history['suit-stack']
        self.historic_row_stack = self.history['row-stack']

        if self.stock_pile != self.historic_stock_pile:
            self.historic_stock_pile = self.stock_pile
        
        if self.waste_pile['top-card'] != self.historic_waste_pile['top-card']:
            locked_cards = self.historic_waste_pile['locked-cards']
            top_card = self.historic_waste_pile['top-card']
            
            locked_cards.append(top_card)
            self.historic_waste_pile['top-card'] = self.waste_pile['top-card']

            ##### OBS! FOR THIS YOU SHOULD CHECK IF CARD HAS MOVED FROM PILE OR IS UNDER
        
        i = 1
        for card in self.suit_stack:
            if self.suit_stack[card] != self.historic_suit_stack[f'suit-{i}']:
                self.historic_suit_stack[f'suit-{i}'] = self.suit_stack[card]
            i += 1

        i = 1
        for stack in self.row_stack:
            index = f'row-{i}'
            new = self.row_stack[stack]['top-card']
            old = self.historic_row_stack[stack]['top-card']

            cardMovedFromStack = ""

            if self.row_stack[stack]['top-card'] != self.historic_row_stack[stack]['top-card']:
                movedToRow = False
                movedToSuit = False

                for tmp_stack in self.historic_row_stack:
                    if self.row_stack[stack]['top-card'] == self.historic_row_stack[tmp_stack]['top-card']:
                        cardMovedFromStack = tmp_stack
                        movedToRow = True
                
                for tmp_suit in self.suit_stack:
                    for tmp_stack in self.historic_row_stack:
                        if self.historic_row_stack[tmp_stack]['top-card'] == self.suit_stack[tmp_suit]:
                            movedToSuit = True

                if movedToRow == True or movedToSuit == True:
                    #Checks if there is no visible cards, remove one from 'remaining' and use that
                    if len(self.historic_row_stack[stack]['visible']) == 0 and self.historic_row_stack[stack]['remaining'] != 0:
                        self.historic_row_stack[stack]['remaining'] -= 1
                        self.historic_row_stack[stack]['top-card'] = self.row_stack[stack]['top-card']
                    
                    ##### OBS - Here it should check if more than one card is moved
                    #if cardMovedFromStack['top-card'] == 
                    
                    
                    #Checks if there is cards in visible stack and choose the first as the next
                    elif len(self.historic_row_stack[stack]['visible']) != 0:
                        #loop through all cards in historic visible
                        for card in self.historic_row_stack[stack]['visible']:
                            if self.row_stack[stack]['top-card'] in self.historic_row_stack[stack]['visible']:
                                self.historic_row_stack[stack]['visible'].remove(self.row_stack[stack]['top-card'])
                                self.historic_row_stack[stack]['top-card'] = self.row_stack[stack]['top-card']
                                continue
                
                elif self.row_stack[stack]["top-card"] == "":
                    self.historic_row_stack[stack]["top-card"] = self.row_stack[stack]['top-card']

                else:
                    self.historic_row_stack[stack]['visible'].append(self.historic_row_stack[stack]['top-card'])
                    self.historic_row_stack[stack]['top-card'] = self.row_stack[stack]['top-card']
                

                ###### OBS: The case where more than one card is moved, isnt handled


            i += 1

        
        with open('boardHistory.json', 'w') as h:
            json.dump(self.history, h)     



    def main(self):
        pass
        
        


    