from Algorithm import cards
from Algorithm.MainPlayFunctions.image_rec_confirmer import confirmCard
from Algorithm.MainPlayFunctions.look_for_unkown_cards import unknownCards
from Algorithm.MainPlayFunctions.mock_input import mockImageRec
from Algorithm.MainPlayFunctions.play_loop import playLoop
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




def game():
    # Initiate start game and load init board
    game_end = False
    next_move = True
    with open('initBoard.json') as f:
        board = json.load(f)
    # First the 7 row stack cards should be confirmed
    # Row-1
    rec_card = mockImageRec()
    actual_card = confirmCard(rec_card)
    board["row-stack"]["row-1"][0] = actual_card
    with open('board.json', 'w') as h:
        json.dump(board, h)
    # Row-2
    with open('board.json') as f:
        board = json.load(f)
    rec_card = mockImageRec()
    actual_card = confirmCard(rec_card)
    board["row-stack"]["row-2"][0] = actual_card
    with open('board.json', 'w') as h:
        json.dump(board, h)
    # Row-3
    with open('board.json') as f:
        board = json.load(f)
    rec_card = mockImageRec()
    actual_card = confirmCard(rec_card)
    board["row-stack"]["row-3"][0] = actual_card
    with open('board.json', 'w') as h:
        json.dump(board, h)
    # Row-4
    with open('board.json') as f:
        board = json.load(f)
    rec_card = mockImageRec()
    actual_card = confirmCard(rec_card)
    board["row-stack"]["row-4"][0] = actual_card
    with open('board.json', 'w') as h:
        json.dump(board, h)
    # Row-5
    with open('board.json') as f:
        board = json.load(f)
    rec_card = mockImageRec()
    actual_card = confirmCard(rec_card)
    board["row-stack"]["row-5"][0] = actual_card
    with open('board.json', 'w') as h:
        json.dump(board, h)
    # Row-6
    with open('board.json') as f:
        board = json.load(f)
    rec_card = mockImageRec()
    actual_card = confirmCard(rec_card)
    board["row-stack"]["row-6"][0] = actual_card
    with open('board.json', 'w') as h:
        json.dump(board, h)
    # Row-7
    with open('board.json') as f:
        board = json.load(f)
    rec_card = mockImageRec()
    actual_card = confirmCard(rec_card)
    board["row-stack"]["row-7"][0] = actual_card
    with open('board.json', 'w') as h:
        json.dump(board, h)

    # Game after start sequence
    while (not game_end) and next_move:
        next_move = False
        # Load latest board
        with open('board.json') as f:
            board = json.load(f)

        # Start move manager
        mm = MoveManager()
        # Create the legal_moves lit
        mm.movables()
        # Strategy manger will then be given the moves
        sm = StrategyManager(mm.legal_moves)
        print("---------------------------------------------")
        if sm.best_move()["moveType"] == 7:
            print("Best move is turning the stockpile ONCE")
        else:
            cardd = sm.best_move()["cards"]
            cards_name = []
            for card in cardd:
                cards_name.append(Cards.getCardName(card))
            location = sm.best_move()["to"]
            print("Move card(s): " + str(cards_name) + ", to: " + str(location))

        next_move_confirm = ""
        print("Confirm that move is performed with ENTER")
        confirmer = input()
        # Perform move on JSON board and save it
        board = mm.doMove(sm.best_move())
        # Then check if any card is -1 and update with image rec if so
        board = unknownCards(board)
        with open('board.json', 'w') as h:
            json.dump(board, h)
        next_move = True


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
        print(f"Possible moves: {mm.legal_moves}")

        ##Init Strategy Manager and pass legal moves from Move Manager
        sm = StrategyManager(mm.legal_moves)

        ##Make move
        board_after_move = mm.doMove(sm.best_move())  ##complete board
        board = hm.update_board(board_after_move)  ##updates the board

        # New input from image rec, then update unknown value in board.json
        print("Waiting for user input:")
        try:
            unknown_card = int(input())  ##Input from user
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
    playLoop()
