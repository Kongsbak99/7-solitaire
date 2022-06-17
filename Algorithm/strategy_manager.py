import json

from Algorithm.cards import Cards



class StrategyManager:

    def __init__(self, moves):
        self.moves = moves

        with open('board.json') as f:
            self.board = json.load(f)

    # Next to do
    # Sort out main calling this function properly instead

    # main method for general flow of strategy manager
    def best_move(self):
        moves = []
        ## Check for suit move
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 4 or self.moves[i]['moveType'] == 1:
                moves.append(self.moves[i])
        if len(moves) > 0:
            best_move = self.suit_stack_move(moves)
            if best_move == 'skip':
                moves = []
            else: return best_move
        ## Check for king move
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 5 or self.moves[i]['moveType'] == 6:
                moves.append(self.moves[i])
        if len(moves) > 0:
            best_move = self.king_move(moves)
            if best_move == 'skip':
                moves = []
            else: return best_move
        ## Check for row move
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 3 or self.moves[i]['moveType'] == 2:
                moves.append(self.moves[i])
        if len(moves) > 0:
            best_move = self.row_stack_move(moves)
            if best_move == 'skip':
                moves = []
            else: return best_move

        ##no moves doesny have a move type yet 
        for i in range(len(self.moves)): 
            if self.moves[i]['moveType'] == 7:
                moves.append(self.moves[i])
        if len(moves) > 0:
            best_move = self.no_moves(moves)
            return best_move

    # This function can probably be ignored
    def suit_stack_move(self, moves):
        
        for move in moves:
            card = move['cards'][0]
            move_card = Cards.getCardValue(card)

            if card == 1 or card == 14 or card == 27 or card == 40 or card == 2 or card == 15 or card == 28 or card == 41:
                return move
            else:
                board = self.board
                count = 0
                for row in board['row-stack']: 
                    if len(board['row-stack'][row]) > 0:
                        row_card = Cards.getCardValue(board['row-stack'][row][0])
                        for card in board['row-stack'][row]:
                            if card != 0:
                                row_card = Cards.getCardValue(card)
                                if row_card == move_card-2:
                                    count = count + 1
                for stack in board['suit-stack']:
                    if len(board['suit-stack'][stack]) > 1:
                        suit_card = Cards.getCardValue(board['suit-stack'][stack][1])

                        if suit_card > move_card or suit_card == move_card or suit_card == move_card-1 or suit_card == move_card-2:
                            count = count + 1

                if count == 3:
                    return move
                else:
                    return 'skip'


    def king_move(self, moves):
        
        ## If stock pile % 3 == 0, we choose the waste pile move, to make sure the stock pile doesnt get locked. 
        for move in moves: 
            if move['moveType'] == 6:
                stock_pile = self.board['stock-pile']
                if len(stock_pile) % 3 == 0:
                    return move
        ## Else we consider the rest of the possible king moves
        ## If more than one king move, we choose the one moving from a pile with more unknown cards. 
        if len(moves) > 1:
            rows = [] ## Rows moves are moved from
            for row in self.board['row-stack']:
                for move in moves:
                    if self.board['row-stack'][row]:
                        ## Check that it is a row (not waste pile)
                        if self.board['row-stack'][row][0] == move['cards'][0]:
                            total_length = len(self.board['row-stack'][row])
                            move_type = move['moveType']
                            unknown_size = 0
                            for card in self.board['row-stack'][row]:
                                if card == 0:
                                    unknown_size = unknown_size + 1
                            rows.append({'moved_from': row, 'moveId': move['moveId'], 'move_type': move_type, 'unknown_size': unknown_size, 'total_length': total_length})
            ## Best move = the move with the most unknowns underneath. 
            best_move = rows[0]
            for row in rows:
                if row['unknown_size'] < best_move['unknown_size']:
                    best_move = row
            for move in moves:
                if move['moveId'] == best_move['moveId']:
                    return move
        
        else: return moves[0] ##If only one move, return that

    def row_stack_move(self, moves):
        ##Check if only move is movetype  2
        movetype_3_found = False
        for move in moves:
            if move['moveType'] == 3:
                movetype_3_found = True
        if movetype_3_found == False: return moves[0]

        # Check if a King is available
        king_available = False
        for row in self.board['row-stack']:
            if self.board['row-stack'][row]:
                card = self.board['row-stack'][row][0]
                if card == 13 or card == 26 or card == 39 or card == 52 and len(self.board['row-stack'][row]) > 1:
                    king_available = True
        if self.board["waste-pile"]:
            if self.board['waste-pile'][0] == 13 or self.board['waste-pile'][0] == 26 or self.board['waste-pile'][0] == 39 or self.board['waste-pile'][0] == 52:
                king_available = True
        
        rows = [] ## Rows moves are moved from
        for row in self.board['row-stack']:
            for move in moves:
                if self.board["row-stack"][row]:
                    if self.board['row-stack'][row][0] == move['cards'][0]:
                        total_length = len(self.board['row-stack'][row])
                        unknown_size = 0
                        for card in self.board['row-stack'][row]:
                            if card == 0:
                                unknown_size = unknown_size + 1
                        rows.append({'moved_from': row, 'moveId': move['moveId'], 'unknown_size': unknown_size, 'total_length': total_length})

        best_move = rows[0]
        if king_available == True:
            ## Check which row is the smallest
            for row in rows:
                if row['total_length'] < best_move['total_length']:
                    best_move = row
        else:       
            ## Check which row has the most 0'
            for row in rows:
                if row['unknown_size'] > best_move['unknown_size']:
                    best_move = row

        if best_move['unknown_size'] == 0 and king_available == False:
            return 'skip'
        else:
            ## Find the best move and return
            for move in moves:
                if move['moveId'] == best_move['moveId']:
                    return move


    # This function can probably be ignored
    def no_moves(self, moves):
        # No moves = The lowest value
        # If no moves available on rows -> Turn stockpile
        # If stockpile has not yet played a card -> Only play 1 card
        # If 1 card from stockpile has been played - Loop through pile until cards have been played

        # If move is available and it creates an empty row
        # Do not move, unless
        # King available
        # No other moves available
        return moves[0]
