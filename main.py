from Algorithm.cards import Cards
from Algorithm.history_manager import HistoryManager
from Algorithm.mock_input import create_mock_input
from Algorithm.move_manager import MoveManager
from Algorithm.strategy_manager import StrategyManager



from ImageRecognition import image



def main():
    # Use a breakpoint in the code line below to debug your script.
    #hm = HistoryManager()
    #mm = MoveManager()
    #sm = StrategyManager()

    #hm.check_history()

    game_end = False
    ##Start game
    hm = HistoryManager(create_mock_input()) ##init game
    ## while game_end == False: ##Keep while loop active, until game is finished. 

    ##After init of board, check for moves
    MoveManager.movables()
    print(MoveManager.legal_moves)

    ##Init Strategy Manager and pass legal moves from Move Manager
    sm = StrategyManager(MoveManager.legal_moves)

    ##Make move
    board_after_move = MoveManager.make_move(sm.best_move())

    hm.update_board(board_after_move)

    ##Send moves to strategy manager 
    # this part of the flow, should end up with an updated board
    # like the one mocked below (notice the -1 value on row 3.)
    mock_strategy_manager_input = {
        "stock-pile": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "waste-pile": [13, 51, 12],
        "suit-stack": {
        "suit-1": [0, 1],
        "suit-2": [0],
        "suit-3": [0],
        "suit-4": [0]
        },
        "row-stack": {
            "row-1": [16],
            "row-2": [4, 0],
            "row-3": [-1, 0],
            "row-4": [18, 0, 0, 0],
            "row-5": [32, 0, 0, 0, 0],
            "row-6": [2, 0, 0, 0, 0, 0],
            "row-7": [10, 0, 0, 0, 0, 0, 0]
        }
    }

    ##Then board should be updated, and ready for next move
    hm.update_board(mock_strategy_manager_input)

    #New input from image rec, then update unknown value in board.json
    new_mock_input = {
        "waste-pile": [13, 51, 12],
        "row-stack": {
            "row-1": 16,
            "row-2": 4,
            "row-3": 5,
            "row-4": 18,
            "row-5": 32,
            "row-6": 2,
            "row-7": 10
        }
    }

    hm.update_board(new_mock_input)
    print("")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
