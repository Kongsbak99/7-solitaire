class StrategyManager:

    def __init__(self, moves):
        self.moves = moves

    # Next to do
    # Need moveTypes specified correctly
    # From waste to Suit, row to Suit = moveType 4
    # From Waste King to Row, Row King to Row = moveType 3
    # From Row to Row = moveType 2
    # From Stockpile to Waste-pile = moveType 1
    # Sort out main calling this function properly instead

    # main method for general flow of strategy manager
    def best_move(self):
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 4:
                print(f"SuitStack MoveType: {self.moves[i]['moveType']}")
                best_moves = self.moves[i]
                print(f"SuitStack Best Moves: {best_moves}")
                return best_moves
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 2:
                print(f"KingStack MoveType: {self.moves[i]['moveType']}")
                best_moves = self.moves[i]
                print(f"KingStack Best Moves: {best_moves}")
                return best_moves
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 3:
                print(f"RowStack MoveType: {self.moves[i]['moveType']}")
                best_moves = self.moves[i]
                print(f"RowStack Best Moves: {best_moves}")
                return best_moves
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 1:
                print(f"NoStack MoveType: {self.moves[i]['moveType']}")
                best_moves = self.moves[i]
                print(f"NoStack Best Moves: {best_moves}")
                return best_moves
        # if len(self.moves) > 0:
            # best_move = self.row_stack_move()  # overwrite best_move
            # best_move = self.king_move()  # overwrite best_move
            # best_move = self.suit_stack_move()  # overwrite best_move
            # print(f"Best move in Strategy Manager If: {best_move}")
        # else:
            # best_move = self.no_moves()  # if moves is empty = no moves
            # print(f"Best move in Strategy Manager Else: {best_move}")
        # return best_moves

    # This function can probably be ignored
    def suit_stack_move(self):
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
        return self.moves[0]

    # This function can probably be ignored
    def king_move(self):
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
        return self.moves

    # This function can probably be ignored
    def row_stack_move(self):
        # Row move = The third-highest value
        # If more than one move available -> The largest card takes precedence
        return self.moves

    # This function can probably be ignored
    def no_moves(self):
        # No moves = The lowest value
        # If no moves available on rows -> Turn stockpile
        # If stockpile has not yet played a card -> Only play 1 card
        # If 1 card from stockpile has been played - Loop through pile until cards have been played

        # If move is available and it creates an empty row
        # Do not move, unless
        # King available
        # No other moves available
        return self.moves
