import json
from operator import contains
import re


class HistoryManager():
    def __init__(self):
        #with open('./board.json') as f:
        #   self.data = json.load(f)

        #with open('boardHistory.json', 'w') as h:
        #    json.dump(self.data, h)
        pass

# Tag imod nyt input med alle face-up
# Primære opgave: Finde ud af hvilke nye kort der er. 
# Er der vendt nyt row-stack kort eller kom det fra waste-pile
    def check_history(self):
        with open('./board.json') as f:
           self.data = json.load(f)

        with open('./boardHistory.json') as f:
           self.history = json.load(f)

        self.stock_pile = self.data['stock-pile']["suit-1"]
        self.waste_pile = self.data['waste-pile']
        self.suit_stack = self.data['suit-stack']
        self.row_stack = self.data['row-stack']

        self.historic_stock_pile = self.history['stock-pile']
        self.historic_waste_pile = self.history['waste-pile']
        self.historic_suit_stack = self.history['suit-stack']
        self.historic_row_stack = self.history['row-stack']

        #Handle change in suit stack
        for stack in self.suit_stack:
            if self.suit_stack[stack] != self.historic_suit_stack[stack]:
                self.historic_suit_stack[stack] = self.suit_stack[stack]

        #Handle new card in waste pile
        if self.waste_pile != self.historic_waste_pile['top-card']:
            old_top = self.historic_waste_pile['top-card']
            moved_to_row = False

            #check if old card is on board. 
            # If not, add to locked cards and make top-card the new card
            for stack in self.row_stack:
                if len(self.row_stack[stack]) > 0:
                    if old_top == self.row_stack[stack][0]:
                        moved_to_row = True
                    else:
                        moved_to_row = False
                else:
                    continue
            
            if moved_to_row == False:
                #First add previous top card to locked cards, then change top-card to new
                self.historic_waste_pile['locked-cards'].append(self.historic_waste_pile['top-card'])
                self.historic_waste_pile['top-card'] = self.waste_pile
            
            if moved_to_row == True:
                #First remove card from locked, then add that card as the top-card
                self.historic_waste_pile['locked-cards'].remove(self.waste_pile)
                self.historic_waste_pile['top-card'] = self.waste_pile
        
        #Handle row stacks
        for stack in self.row_stack:
            #new = self.row_stack[stack]['top-card']
            #old = self.historic_row_stack[stack]['top-card']

            # Create a tmp stack to use for comparison with the new row_stacks
            _hist_stack = []
            for card in self.historic_row_stack[stack]:
                if card != 0:
                    _hist_stack.append(card)

            # Compare old and new stacks
            if self.row_stack[stack] != _hist_stack:
                #Find all 0's in old stack, so we can add them later (these are the face down cards)
                _facedown_cards =[] 
                for card in self.historic_row_stack[stack]:
                    if card == 0:
                        _facedown_cards.append(card)
                
                # Make old stack = new stack
                self.historic_row_stack[stack] = self.row_stack[stack]

                #If length of stack is > 1, that would mean that no new card has been turned over
                #And therefore the stack has grown
                #OBS: hist is now updated to new
                if len(self.historic_row_stack[stack]) > 1:
                    for facedown in _facedown_cards:
                        self.historic_row_stack[stack].append(facedown)
                
                #If length is less than 2, it would mean that either its empty or only one card is there
                #If only one card, that would mean a new card is available in that row. If one or more facedown cards exists
                #That would mean the new card comes from a facedown card
                elif len(self.historic_row_stack[stack]) < 2:
                    # If any facedown cards, remove one.
                    if len(_facedown_cards) > 0:
                        _facedown_cards.pop()
                        #If more facedown cards are left, add them to the stack again.
                        if len(_facedown_cards) > 0:
                            for facedown in _facedown_cards:
                                self.historic_row_stack[stack].append(facedown)
                    elif len(_facedown_cards) == 0:
                        # In case of no facedown cards. 
                        continue



        #if self.stock_pile != self.historic_stock_pile:
        #    self.historic_stock_pile = self.stock_pile
        #
        #if self.waste_pile['top-card'] != self.historic_waste_pile['top-card']:
        #    locked_cards = self.historic_waste_pile['locked-cards']
        #    top_card = self.historic_waste_pile['top-card']
        #    
        #    locked_cards.append(top_card)
        #    self.historic_waste_pile['top-card'] = self.waste_pile['top-card']

        #    ##### OBS! FOR THIS YOU SHOULD CHECK IF CARD HAS MOVED FROM PILE OR IS UNDER
        #
        #i = 1
        #for card in self.suit_stack:
        #    if self.suit_stack[card] != self.historic_suit_stack[f'suit-{i}']:
        #        self.historic_suit_stack[f'suit-{i}'] = self.suit_stack[card]
        #    i += 1

        #i = 1
        #for stack in self.row_stack:
        #    new = self.row_stack[stack]['top-card']
        #    old = self.historic_row_stack[stack]['top-card']

        #    movedFromStack = ""

        #    if self.row_stack[stack]['top-card'] != self.historic_row_stack[stack]['top-card']:
        #        movedToRow = False
        #        movedToSuit = False

        #        for tmp_stack in self.historic_row_stack:
        #            if self.row_stack[stack]['top-card'] == self.historic_row_stack[tmp_stack]['top-card']:
        #                cardMovedFromStack = tmp_stack
        #                movedToRow = True
                
        #        for tmp_suit in self.suit_stack:
        #            for tmp_stack in self.historic_row_stack:
        #                if self.historic_row_stack[tmp_stack]['top-card'] == self.suit_stack[tmp_suit]:
        #                    movedToSuit = True

        #        if movedToRow == True or movedToSuit == True:

        #            if len(self.historic_row_stack[movedFromStack]['visible'] > 0):
                        #loop through visible card in prev stack
                        #Check if card in visible is == to top card in new stack. 
                        #If last card in visible stack
        #                pass

                        



                    #Checks if there is no visible cards, remove one from 'remaining' and use that
                    #if len(self.historic_row_stack[stack]['visible']) == 0 and self.historic_row_stack[stack]['remaining'] != 0:
                    #    self.historic_row_stack[stack]['remaining'] -= 1
                    #    self.historic_row_stack[stack]['top-card'] = self.row_stack[stack]['top-card']
                    
                    ##### OBS - Here it should check if more than one card is moved
                    #if cardMovedFromStack['top-card'] == 
                    
                    
                    #Checks if there is cards in visible stack and choose the first as the next
                    #elif len(self.historic_row_stack[stack]['visible']) != 0:
                    #    #loop through all cards in historic visible
                    #    for card in self.historic_row_stack[stack]['visible']:
                    #        if self.row_stack[stack]['top-card'] in self.historic_row_stack[stack]['visible']:
                    #            self.historic_row_stack[stack]['visible'].remove(self.row_stack[stack]['top-card'])
                    #            self.historic_row_stack[stack]['top-card'] = self.row_stack[stack]['top-card']
                    #            continue
        #            pass
                
        #        elif self.row_stack[stack]["top-card"] == "":
        #            self.historic_row_stack[stack]["top-card"] = self.row_stack[stack]['top-card']

        #        else:
        #            self.historic_row_stack[stack]['visible'].append(self.historic_row_stack[stack]['top-card'])
         #           self.historic_row_stack[stack]['top-card'] = self.row_stack[stack]['top-card']
                

                ###### OBS: The case where more than one card is moved, isnt handled


        #    i += 1

        
        with open('boardHistory.json', 'w') as h:
            json.dump(self.history, h)     



    def main(self):
        pass
        
        


    