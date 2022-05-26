

class StrategyManager():
    
    def __init__(self, moves):
        self.moves = moves

    def best_move(self):
        return self.moves[0]
    
