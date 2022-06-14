import random


def mockImageRec():
    return random.randint(1, 52)



def init_mock_input():
    
    mock_input = {
    "waste-pile": [52],
    "row-stack": {
        "row-1": 12,
        "row-2": 18,
        "row-3": 16,
        "row-4": 26,
        "row-5": 3,
        "row-6": 30,
        "row-7": 37
      }
    }
    
    return mock_input
