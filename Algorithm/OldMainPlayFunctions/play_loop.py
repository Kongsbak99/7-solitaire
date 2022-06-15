import json

from Algorithm.MainPlayFunctions.look_for_unkown_cards import unknownCards
from Algorithm.MainPlayFunctions.start_rows import startRows
from Algorithm.cardss import Cardss
from Algorithm.move_manager import MoveManager
from Algorithm.strategy_manager import StrategyManager


def playLoop():
    # Read init board
    with open('initBoard.json') as f:
        board = json.load(f)
        f.close()
    f.close()

    active_game = True
    next_move = True

    # Start by reading the first 7 cards and save the new board
    board = startRows(board)

    with open('board.json', 'w') as h:
        json.dump(board, h)
        h.close()
    h.close()

    # Play loop
    while active_game and next_move:
        next_move = False
        # Load latest board
        with open('board.json') as f:
            board = json.load(f)
            f.close()
        f.close()
        print("PlayLoop: " + str(board))

        # Start new move manager
        mm = MoveManager()
        # Create the legal_moves list
        mm.movables()
        # Start the strategy manager and give it the legal_moves list
        sm = StrategyManager(mm.legal_moves)

        print("---------------------------------------------")

        # Check the best move
        if sm.best_move()["moveType"] == 7:
            print("Best move is turning the stockpile ONCE")
        else:
            cards = sm.best_move()["cards"]
            cards_name = []
            for card in cards:
                cards_name.append(Cardss.getCardName(card))
            location = sm.best_move()["to"]
            print("Best move is moving card(s): " + str(cards_name) + ", to " + str(location))

        print("Confirm that move is performed with ENTER")
        input_confirmer = input()
        # Perform move on JSON board and save it
        mm.doMove(sm.best_move())

        # Reload board and check for -1 cards and update with image rec
        with open('board.json') as f:
            board = json.load(f)
            f.close()
        f.close()
        print("-1 load: " + str(board))
        board = unknownCards(board)
        with open('board.json', 'w') as h:
            json.dump(board, h)
            h.close()
        h.close()
        print("-1 gem: " + str(board))

        next_move = True


