import json

from Algorithm.PlayLoopFunctions.mock_input import imgrec_service
from Algorithm.history_manager import HistoryManager, findUnknownCard
from Algorithm.move_manager import MoveManager
from Algorithm.strategy_manager import StrategyManager
from ImageRecognition.CardDetection import ObjectDetection
from ImageRecognition.edgeDetectionLive2 import GetCardCorner
from ImageRecognition.write_on_image import write_on_image
import cv2
from ImageRecognition.imageSplit import draw_boxes
from Algorithm.cardss import Cardss as Cardss

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


class Cards:
    def __init__(self, row, card):
        self.row = row
        self.card = card


# Finds card in specific box.
# i = 0..11 (location of the card frame)
# listOfCorers = array of all card frames
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
            for y in range(3):  # int is amount of times it tries again, if no card is found
                card = getCard(i, listOfCorners)  # Finds the card in the box
                if "null" != card:
                    break
                print("trying again")
            listofResults.append(Cards(i, card))  # Adds the found card to the list
    except:
        print("could not append to list")

    print("Printing list of cards")
    for obj in listofResults:
        print(str(obj.row) + " " + obj.card)
    return listofResults


# function to run image recognition and returns list of all cards on board
def runAllCards(frame, framenum, listofResults):
    # _, frame = cap.read()
    listOfFrames = draw_boxes(frame)  # separates frames
    # cv2.imshow('preview', frame)

    if framenum == -1:
        listofResults = run(listOfFrames)
    else:
        try:
            listOfCorners = []
            for i in range(len(listOfFrames)):
                listOfCorners.append(GetCardCorner(listOfFrames[i]))
        except:
            print("could not find card corner")
        try:
            listofResults[framenum] = Cards(framenum, getCard(framenum, listOfCorners))
        except:
            print("error finding new card in frame: " + framenum)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
    return listofResults


def showImage(frame, listofResults):
    #if len(listofResults) > 1:
        # print("length is > 1... Showing found cards on image")
#        for i in range(len(listofResults)):
            #write_on_image(frame, listofResults[i].row, listofResults[i].card)
    draw_boxes(frame)  # draws boxes
    cv2.imshow('preview', frame)


def setup():
    while 1:
        _, frame = cap.read()
        draw_boxes(frame)
        cv2.imshow('preview', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            break


def main():
    ##initiate start game
    game_end = False
    listofResults = []

    # TODO fjern init_input her:
    # init_input = init_mock_input()

    # TODO Fjern hashtag på de 2 linjer under og ændre imgrec_input = deres imgrec metode
    _, frame = cap.read()
    showImage(frame, listofResults)
    imgrec_input = runAllCards(frame, -1, [])  # TODO i stedet for imgrec_metode(), deres imgrec metode metode
    listofResults = imgrec_input
    showImage(frame, listofResults)
    # time.sleep(1)
    init_input = imgrec_service(imgrec_input)
    hm = HistoryManager(init_input)  ##init game
    with open('board.json') as f:
        board = json.load(f)
        f.close()
    f.close()

    print("Best move is turning the stockpile ONCE")
    confirmer = input()

    prev_moves = []
    #### General flow of game
    while game_end == False:  ##Keep while loop active, until game is finished.
        ##TODO: Check for lost game

        mm = MoveManager()
        ##After init of board, check for moves
        mm.movables()
        legal_moves = mm.legal_moves
        print(f"Possible moves in Main: {legal_moves}")
        print("")

        if len(prev_moves) > 0:
            removed = []
            for legal_move in legal_moves:
                count = 0
                if 'cards' in legal_move:
                    for move in prev_moves:
                        if legal_move['to'] == move['to'] and legal_move['cards'] == move['cards']:
                            count = count + 1
                if count > 1:
                    removed.append(legal_move)
            for move in removed:
                legal_moves.remove(move)

        ##Init Strategy Manager and pass legal moves from Move Manager
        sm = StrategyManager(legal_moves)
        # Check the best move
        next_move_string = "Best move is turning the stockpile ONCE"
        best_move = sm.best_move()

        if best_move["moveType"] == 7:
            print("Best move is turning the stockpile ONCE")
        else:
            cards = best_move["cards"]
            cards_name = []
            for card in cards:
                cards_name.append(Cardss.getCardName(card))
            location = sm.best_move()["to"]
            next_move_string = "Best move is moving card(s): " + str(cards_name) + ", to " + str(location)
            print(next_move_string)

        write_on_image(frame, -1, next_move_string)
        showImage(frame, listofResults)
        _, frame = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
        print("Confirm that move is performed with ENTER")
        input_confirmer = input()

        # Nyt billede
        #listofResults.clear()
        write_on_image(frame, 7, "")
        showImage(frame, listofResults)
        _, frame = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()

        _, frame = cap.read()

        ##Make move
        board_after_move = mm.doMove(sm.best_move())  ##complete board
        print("Board after move")
        ##Finally update board to new state
        # But only if there's a new unrec'ed card
        unknown_found = False
        if -1 in board_after_move["waste-pile"]:
            unknown_found = True
        for row in board_after_move['row-stack']:
            if -1 in board_after_move['row-stack'][row]:
                unknown_found = True
        if unknown_found:
            unknown_card = findUnknownCard(board_after_move)

            listofResults = runAllCards(frame, unknown_card, listofResults)
            showImage(frame, listofResults)  # SHOULD show found cards on image
            _, frame = cap.read()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                cap.release()

        new_input = hm.update_board(board_after_move, listofResults)

        print("Board after update")

        # Check for victory
        game_end = hm.check_for_victory()
        if 'cards' in best_move:
            prev_moves.append(best_move)
        if len(prev_moves) > 20:
            prev_moves.pop(0)
        print("###################################")

    print("Game ended")


if __name__ == '__main__':
    #setup()
    main()
