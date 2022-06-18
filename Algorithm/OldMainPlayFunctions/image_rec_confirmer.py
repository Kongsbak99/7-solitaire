from threading import Timer

from Algorithm.cardss import Cardss


def confirmCard(card):
    timeout = 5
    t = Timer(timeout, print, ['\nCard NOT confirmed\nEnter actual cardID'])
    t.start()
    print("---------------------------------------------")
    prompt = "Card read as " + str(Cardss.getCardName(card)) + "\nPress ENTER to confirm [%d seconds timeout]" % timeout
    answer = input(prompt)
    t.cancel()

    if answer == "":
        print(str(Cardss.getCardName(card)) + " confirmed")
    else:
        card = int(answer)
        print("Actual cardID set as " + str(Cardss.getCardName(card)))

    return card
