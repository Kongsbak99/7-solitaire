import json



class StrategyManager:

    def __init__(self, moves):
        self.moves = moves

        with open('board.json') as f:
            self.board = json.load(f)

    # Next to do
    # Need moveTypes specified correctly
    # From waste to Suit, row to Suit = moveType 4
    # From Waste King to Row, Row King to Row = moveType 3
    # From Row to Row = moveType 2
    # From Stockpile to Waste-pile = moveType 1
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
            return best_move
        ## Check for king move
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 5 or self.moves[i]['moveType'] == 6:
                moves.append(self.moves[i])
        if len(moves) > 0:
            best_move = self.king_move(moves)
            return best_move
        ## Check for row move
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 3 or self.moves[i]['moveType'] == 2:
                moves.append(self.moves[i])
        if len(moves) > 0:
            best_move = self.row_stack_move(moves)
            return best_move

        ##no moves doesny have a move type yet 
        for i in range(len(self.moves)): 
            if self.moves[i]['moveType'] == 7:
                moves.append(self.moves[i])
        if len(moves) > 0:
            best_move = self.no_moves(moves)
            return best_move

    # This function can probably be ignored
    def suit_stack_move(self, moves):
        # Basic Strategy
        # Suit stack move = The highest value
        # Is suit stack available?
        # If yes -> return this move
        # Advanced strategy
        # Is suit stack available?
        # If yes -> is cardValue-2 for all suits in play?
        # If yes -> move to suit stack
        # If no -> ignore move
        # If no and no other moves available -> return this move
        return moves[0]

    # This function can probably be ignored
    def king_move(self, moves):
        
        
        for move in moves: 
            if move['moveType'] == 6:
                test = 3 % 20
                print("")

        if len(moves) > 1:
            rows = [] ## Rows moves are moved from
            for row in self.board['row-stack']:
                for move in moves:
                    if self.board['row-stack'][row]:
                        if self.board['row-stack'][row][0] == move['cards'][0]:
                            total_length = len(self.board['row-stack'][row])
                            move_type = self.board['row-stack'][row]
                            unknown_size = 0
                            for card in self.board['row-stack'][row]:
                                if card == 0:
                                    unknown_size = unknown_size + 1
                            rows.append({'moved_from': row, 'moveId': move['moveId'], 'move_type': move_type, 'unknown_size': unknown_size, 'total_length': total_length})
            ## Best move = the move with the most unknowns underneath. 
            best_move = rows[0]
            for row in rows:
                if row['unknown_size'] > best_move['unknown_size']:
                    best_move = row
            return best_move
        else: return moves[0]
        print("")
        
        
        
        
        # King move = The second-highest value
        # Is king present on table?
        # If no -> Begin clearing the largest row
        # If yes
        # Is empty row on table?
        # If yes -> move king to empty row
        # If no -> clear smallest row to make room for King

        # If multiple suit Kings and empty row available
        # Check Queens
        # If multiple suit Queens available
        # Check Jacks
        # If multiple suit Jacks available
        # Check Tens
        # If multiple suit Tens available
        # Check Nines
        # If multiple suit Nines available
        # Check Eights
        # If multiple suit Eights available
        # Check Sevens
        # If multiple suit Sevens available
        # Check Sixes
        # If multiple suit Sixes available
        # Check Fives
        # If multiple suit Fives available
        # Check Fours
        # If multiple suit Fours available
        # Check Threes
        # If multiple suit Threes available
        # Check Twos
        # If multiple suit Twos available
        # Pick lowest ID 2
        return moves[0]

    # This function can probably be ignored
    def row_stack_move(self, moves):
        # Check if a King is available
        king_available = False
        for row in self.board['row-stack']:
            if self.board['row-stack'][row]:
                card = self.board['row-stack'][row][0]
                if card == 13 or card == 26 or card == 39 or card == 52 and len(self.board['row-stack'][row]) > 1:
                    king_available = True
        if self.board['waste-pile'][0] == 13 or self.board['waste-pile'][0] == 26 or self.board['waste-pile'][0] == 39 or self.board['waste-pile'][0] == 52:
            king_available = True
        
        if len(moves) > 1:
            rows = [] ## Rows moves are moved from
            for row in self.board['row-stack']:
                for move in moves:
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

            ## Find the best move and return
            for move in moves:
                if move['moveId'] == best_move['moveId']:
                    return move
            
        else:
            return moves[0]

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
