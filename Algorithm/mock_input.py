import json
from operator import contains
import re
from unittest import mock

def init_mock_input():
    
    mock_input = {
    "waste-pile": [0, 0, 0],
    "row-stack": {
        "row-1": 33,
        "row-2": 44,
        "row-3": 17,
        "row-4": 36,
        "row-5": 1,
        "row-6": 34,
        "row-7": 22
      }
    }
    
    return mock_input

def mock_image_rec(board, unknown):

  mock_input = {
    "waste-pile": board['waste-pile'],
    "row-stack": board['row-stack']
  }

  if len(unknown) > 1: ## = new waste pile
    mock_input['waste-pile'] = unknown
  else:
    for i in mock_input['waste-pile']:
      if i == -1:
        i = unknown[0]
    for row in mock_input['row-stack']:
      if mock_input['row-stack'][row][0] == -1:
        mock_input['row-stack'][row][0] = unknown[0]
  
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
