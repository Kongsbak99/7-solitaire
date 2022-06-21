from threading import Timer
from time import sleep

from Algorithm.cardss import Cardss as Cardss


def confirmCard(card):

    print("---------------------------------------------")
    print("Card read as " + str(Cardss.getCardName(card)))
    print("---------------------------------------------")
    sleep(1)

    # timeout = 5
    # t = Timer(timeout, print, ['\nCard NOT confirmed\nEnter actual cardID'])
    # t.start()
    # print("---------------------------------------------")
    # prompt = "Card read as " + str(Cardss.getCardName(card)) + "\nPress ENTER to confirm [%d seconds timeout]" % timeout
    # answer = input(prompt)
    # t.cancel()
    #
    # if answer == "":
    #     print(str(Cardss.getCardName(card)) + " confirmed")
    # else:
    #     card = int(answer)
    #     print("Actual cardID set as " + str(Cardss.getCardName(card)))

    return card
