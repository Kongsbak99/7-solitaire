from Algorithm.cards import Cards
from Algorithm.history_manager import HistoryManager
from Algorithm.mock_input import create_mock_input, mock_image_rec
from Algorithm.move_manager import MoveManager
from Algorithm.strategy_manager import StrategyManager

import json



from ImageRecognition import image



def main():

    game_end = False

    ##Start game
    hm = HistoryManager(create_mock_input()) ##init game
    with open('board.json') as f:
        board = json.load(f)
    
    while game_end == False: ##Keep while loop active, until game is finished. 
        mm = MoveManager()
        ##After init of board, check for moves
        mm.movables()
        print(mm.legal_moves)

        ##Init Strategy Manager and pass legal moves from Move Manager
        sm = StrategyManager(mm.legal_moves)

        ##Make move
        board_after_move = mm.make_move(sm.best_move(), board) ##complete board
        board = hm.update_board(board_after_move) ##updates the board 

        #New input from image rec, then update unknown value in board.json
        print("Waiting for user input:")
        unknown_card = int(input())
        new_mock_input = mock_image_rec(board_after_move, unknown_card)
        print("user input accepted")

        ##Finally update board to new state
        board = hm.update_board(new_mock_input) ##update board



if __name__ == '__main__':
    main()

