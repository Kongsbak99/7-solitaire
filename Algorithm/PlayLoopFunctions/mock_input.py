import random

from Algorithm.cards import Cards


def mockImageRec():
    return random.randint(1, 52)


def init_mock_input():
    
    mock_input = {
    "waste-pile": [33],
    "row-stack": {
        "row-1": 12,
        "row-2": 8,
        "row-3": 12,
        "row-4": 12,
        "row-5": 12,
        "row-6": 12, 
        "row-7": 12
      }
    }

    return mock_input


def imgrec_service(input):
  #test= input[7]
  #waste_id = Cards.getCardId(input[7].card)
  final_input = {
    "waste-pile": [Cards.getCardId(input[7].card)],
    "row-stack": {
        "row-1": Cards.getCardId(input[0].card),
        "row-2": Cards.getCardId(input[1].card),
        "row-3": Cards.getCardId(input[2].card),
        "row-4": Cards.getCardId(input[3].card),
        "row-5": Cards.getCardId(input[4].card),
        "row-6": Cards.getCardId(input[5].card),
        "row-7": Cards.getCardId(input[6].card)
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
