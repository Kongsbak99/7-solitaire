import random

from Algorithm.cardss import Cardss


def mockImageRec():
    return random.randint(1, 52)


def init_mock_input():
    
    mock_input = {
    "waste-pile": [45],
    "row-stack": {
        "row-1": 10,
        "row-2": 17,
        "row-3": 3,
        "row-4": 11,
        "row-5": 24,
        "row-6": 25,
        "row-7": 23
      }
    }

    return mock_input


def imgrec_service(input):
  #test= input[7]
  #waste_id = Cards.getCardId(input[7].card)
  final_input = {
    "waste-pile": [Cardss.getCardId(input[7].card)],
    "row-stack": {
        "row-1": Cardss.getCardId(input[0].card),
        "row-2": Cardss.getCardId(input[1].card),
        "row-3": Cardss.getCardId(input[2].card),
        "row-4": Cardss.getCardId(input[3].card),
        "row-5": Cardss.getCardId(input[4].card),
        "row-6": Cardss.getCardId(input[5].card),
        "row-7": Cardss.getCardId(input[6].card)
      }
    }
    
  return final_input



def mock():
  response = [] 
  cards = ["DK", "S2", "CA", "C2", "C3", "C4", "SA", "H8", "HK", "SK", "SQ"]
  class card():
    def __init__(self, row, card):
        self.row = row
        self.card = card

  for i in range(11):
    response.append(card(i, cards[i]))

  return response
