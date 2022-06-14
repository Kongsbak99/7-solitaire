from threading import Timer

from Algorithm.cards import Cards


def confirmCard(card):
    timeout = 5
    t = Timer(timeout, print, ['\nCard NOT confirmed\nEnter actual cardID'])
    t.start()
    print("---------------------------------------------")
    prompt = "Card read as " + str(Cards.getCardName(card)) + "\nPress ENTER to confirm [%d seconds timeout]" % timeout
    answer = input(prompt)
    t.cancel()

    if answer == "":
        print(str(Cards.getCardName(card)) + " confirmed")
    else:
        card = int(answer)
        print("Actual cardID set as " + str(Cards.getCardName(card)))

    return card
