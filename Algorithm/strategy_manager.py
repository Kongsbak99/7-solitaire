

class StrategyManager():
    
    def __init__(self, moves):
        self.moves = moves

    #main method for general flow of strategy manager
    def best_move(self):
        if len(self.moves) > 0:
            best_move = self.row_stack_move() ##overwrite best_move
            best_move = self.king_move() ##overwrite best_move
            best_move = self.suit_stack_move() ##overwrite best_move
        else: best_move = self.no_moves() #if moves is empty = no moves

        return best_move

    def row_stack_move(self):
        return self.moves[0]
    

    def king_move(self):
        return self.moves[0]


    def suit_stack_move(self):
        return self.moves[0]


    def no_moves(self):
        return self.moves
    
