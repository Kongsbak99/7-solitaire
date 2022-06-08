from Algorithm.cards import Cards
from Algorithm.history_manager import HistoryManager
from Algorithm.mock_input import init_mock_input, mock_image_rec
from Algorithm.move_manager import MoveManager
from Algorithm.strategy_manager import StrategyManager

from Algorithm.MoveTypes.turn_stockpile import turnStockpile

import json

from ImageRecognition import image


def tester():
    moma = MoveManager()
    with open('./board.json') as f:
        brt = json.load(f)
    print("----- Available moves: ------")
    moma.movables()
    moves = moma.legal_moves
    print(moves)

    print('Enter moveId you wish to perfom or "ts" to turn stockpile:')
    user_input = input().lower()
    if user_input == "ts":
        print("--- Turning stock-/wastepile -----")
        braet = turnStockpile(brt)
    else:
        print("--- Performing move -----")
        braet = moma.doMove(moves[int(user_input)])

    with open('board.json', 'w') as h:
        json.dump(braet, h)
    print("--- Please check board.json, and update a unknown card, if any -----")


def main():
    ##initiate start game
    game_end = False
    ##TODO: init_input should come from image rec
    ##If necessary we should reformat input to be same format as mock_init_input()
    init_input = init_mock_input()
    hm = HistoryManager(init_input)  ##init game
    with open('board.json') as f:
        board = json.load(f)

    #### General flow of game
    while game_end == False:  ##Keep while loop active, until game is finished.
        ##TODO: Check for lost game

        mm = MoveManager()
        ##After init of board, check for moves
        mm.movables()
        print(f"Possible moves: {mm.legal_moves}")

        ##Init Strategy Manager and pass legal moves from Move Manager
        sm = StrategyManager(mm.legal_moves)

        ##Make move
        board_after_move = mm.make_move(sm.best_move(), board)  ##complete board
        board = hm.update_board(board_after_move)  ##updates the board

        # New input from image rec, then update unknown value in board.json
        print("Waiting for user input:")
        try:
            unknown_card = list(map(int, input().split()))  ##Input from user
            new_input = mock_image_rec(board_after_move,
                                       unknown_card)  ##What it should look like from image rec (we can reformat to look like this if necessary)
        except Exception as e:
            print(f"Error in image rec input: {e}")
        print("user input accepted")

        ##Finally update board to new state
        board = hm.update_board(new_input)  ##update board

        # Check for victory
        game_end = hm.check_for_victory()
    print("Game ended")


if __name__ == '__main__':
    tester()
