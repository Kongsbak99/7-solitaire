import json
from operator import contains


class HistoryManager():
    def __init__(self):
        #with open('./board.json') as f:
        #   self.data = json.load(f)

        #with open('boardHistory.json', 'w') as h:
        #    json.dump(self.data, h)
        pass


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
        
        for card in self.suit_stack:
            i = 1
            if card != self.historic_suit_stack[f'suit-{i}']:
                self.historic_suit_stack[f'suit-{i}'] = card
            i += 1

        i = 1
        for stack in self.row_stack:
            index = f'row-{i}'
            new = self.row_stack[stack]['top-card']
            old = self.historic_row_stack[index]['top-card']
            if self.row_stack[stack]['top-card'] != self.historic_row_stack[index]['top-card']:
                movedToRow = False
                movedToSuit = False

                for tmp_stack in self.row_stack:
                    if self.row_stack[tmp_stack]['top-card'] == self.historic_row_stack[index]['top-card']:
                        movedToRow = True
                
                for card in self.suit_stack:
                    if card == self.historic_row_stack[index]['top-card']:
                        movedToSuit = True

                if movedToRow == True or movedToSuit == True:
                    if len(self.historic_row_stack[index]['visible']) == 0 and self.historic_row_stack[index]['remaining'] != 0:
                        self.historic_row_stack[index]['remaining'] -= 1
                        self.historic_row_stack[index]['top-card'] = self.row_stack[stack]['top-card']

                    elif len(self.historic_row_stack[index]['visible']) != 0:
                        self.historic_row_stack[index]['visible'].remove(self.row_stack[stack]['top-card'])
                        self.historic_row_stack[index]['top-card'] = self.row_stack[stack]['top-card']

                else:
                    self.historic_row_stack[index]['visible'].append(self.historic_row_stack[f'row-{i}']['top-card'])
                    self.historic_row_stack[index]['top-card'] = self.row_stack[stack]['top-card']
            
            i += 1



        
        with open('boardHistory.json', 'w') as h:
            json.dump(self.history, h)

        
        



    def main(self):
        pass
        
        


    