import json
import os
import random

from matplotlib import pyplot as plt

from Algorithm.PlayLoopFunctions.mock_input import imgrec_service
from Algorithm.history_manager import HistoryManager
from Algorithm.move_manager import MoveManager
from Algorithm.strategy_manager import StrategyManager
from ImageRecognition.CardDetection import ObjectDetection
from ImageRecognition.edgeDetectionLive2 import GetCardCorner
from ImageRecognition.write_on_image import write_on_image
import cv2
from ImageRecognition.imageSplit import navn
from Algorithm.cardss import Cardss as Cardss

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


class Cards:
    def __init__(self, row, card):
        self.row = row
        self.card = card



def getCard(i, listOfCorners):
    try:
        detector = ObjectDetection(capture_index=listOfCorners[i], model_name=True)
        card = detector()
        return card
    except:
        print("error")
        return "H6"

def run(listOfFrames):
    listOfCorners = []
    listofResults = []
    listofResults.clear()

    try:
        for i in range(len(listOfFrames)):
            listOfCorners.append(GetCardCorner(listOfFrames[i]))
    except:
        print("could not find card corner")

    # Create a new object and execute.
    try:
        for i in range(len(listOfCorners)):
            for y in range(2):
                card = getCard(i, listOfCorners)
                if "null" != card:
                    break
                print("trying again")

            listofResults.append(Cards(i, card))
    except:
        print("could not append to list")

    print("Printing list of cards")
    for obj in listofResults:
        print(str(obj.row) + " " + obj.card)
    return listofResults

def runAllCards(cap):

    _, frame = cap.read()
    listOfFrames = navn(frame)
    cv2.imshow('preview', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cap.release()

    listofResults = run(listOfFrames)
    for i in range(len(listofResults)):
        write_on_image(frame, listofResults[i].row, listofResults[i].card)
    cv2.imshow('preview', frame)
    return listofResults

    # if cv2.waitKey(1) & 0xFF == ord('r'):
    #     cv2.imshow('preview', frame)
    #     run()

def setup():
    while 1:
        _, frame = cap.read()
        listOfFrames = navn(frame)
        cv2.imshow('preview', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

def main():


    print("IVE BEEN RUN")
    ##initiate start game
    game_end = False

    #TODO fjern init_input her:
    # init_input = init_mock_input()

    #TODO Fjern hashtag på de 2 linjer under og ændre imgrec_input = deres imgrec metode
    imgrec_input = runAllCards(cap) # TODO i stedet for imgrec_metode(), deres imgrec metode metode
    #time.sleep(1)
    init_input = imgrec_service(imgrec_input)
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

        print("ppp")
        # Nyt billede
        _, frame = cap.read()

        ##Make move
        board_after_move = mm.doMove(sm.best_move())  ##complete board
        print("Board after move")
        ##Finally update board to new state
        new_input = hm.update_board(board_after_move, runAllCards(cap))
        print("Board after update")

        # Check for victory
        game_end = hm.check_for_victory()

        print("###################################")
    print("Game ended")

if __name__ == '__main__':
    #setup()
    main()
    #runmycards(cap)
    #time.sleep(25)

