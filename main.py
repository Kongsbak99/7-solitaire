#from Algorithm.MainPlayFunctions.image_rec_confirmer import confirmCard
from Algorithm.OldMainPlayFunctions.new_look_for_unkown_cards import unknownCards
#from Algorithm.MainPlayFunctions.mock_input import mockImageRec
#from Algorithm.MainPlayFunctions.play_loop import playLoop
from Algorithm.cards import Cards
from Algorithm.history_manager import HistoryManager
from Algorithm.OldMainPlayFunctions.old_mock_input import init_mock_input
from Algorithm.move_manager import MoveManager
from Algorithm.strategy_manager import StrategyManager

from Algorithm.PlayLoopFunctions.image_rec_confirmer import confirmCard
from Algorithm.PlayLoopFunctions.mock_input import mockImageRec

from Algorithm.MoveTypes.turn_stockpile import turnStockpile

import json

from ImageRecognition import image


def main():
    ##initiate start game
    game_end = False
    ##TODO: init_input should come from image rec
    ##If necessary we should reformat input to be same format as mock_init_input()
    init_input = init_mock_input()
    hm = HistoryManager(init_input)  ##init game
    with open('board.json') as f:
        board = json.load(f)
        f.close()
    f.close()


    #### General flow of game
    while game_end == False:  ##Keep while loop active, until game is finished.
        ##TODO: Check for lost game

        mm = MoveManager()
        ##After init of board, check for moves 
        mm.movables()
        print(f"Possible moves in Main: {mm.legal_moves}")
        print("")

        ##Init Strategy Manager and pass legal moves from Move Manager
        sm = StrategyManager(mm.legal_moves)
        best_move = sm.best_move()
        print(f"Best move: {best_move}")

        ##Make move
        board_after_move = mm.doMove(sm.best_move())  ##complete board
        ##Finally update board to new state
        new_input = hm.update_board(board_after_move)

        # Check for victory
        game_end = hm.check_for_victory()


    print("Game ended")


if __name__ == '__main__':
    main()
