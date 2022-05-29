import json
from operator import contains
import re

def create_mock_input():
    
    mock_input = {
    "waste-pile": [13, 51, 12],
    "row-stack": {
        "row-1": 16,
        "row-2": 4,
        "row-3": 1,
        "row-4": 18,
        "row-5": 32,
        "row-6": 2,
        "row-7": 10
    }
  }
    
    return mock_input

def mock_image_rec(board, unknown):

  mock_input = {
    "waste-pile": board['waste-pile'],
    "row-stack": board['row-stack']
  }

  for i in mock_input['waste-pile']:
    if i == -1:
      i = unknown
  for row in mock_input['row-stack']:
    if mock_input['row-stack'][row][0] == -1:
      mock_input['row-stack'][row][0] = unknown
  
  return {
    "waste-pile": mock_input['waste-pile'],
    "row-stack": {
        "row-1": mock_input['row-stack']['row-1'][0],
        "row-2": mock_input['row-stack']['row-2'][0],
        "row-3": mock_input['row-stack']['row-3'][0],
        "row-4": mock_input['row-stack']['row-4'][0],
        "row-5": mock_input['row-stack']['row-5'][0],
        "row-6": mock_input['row-stack']['row-6'][0],
        "row-7": mock_input['row-stack']['row-7'][0]
    }
  }
