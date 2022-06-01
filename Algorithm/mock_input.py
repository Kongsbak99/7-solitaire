import json
from operator import contains
import re
from unittest import mock

def init_mock_input():
    
    mock_input = {
    "waste-pile": [41, 2, 8],
    "row-stack": {
        "row-1": 1,
        "row-2": 18,
        "row-3": 50,
        "row-4": 14,
        "row-5": 5,
        "row-6": 12,
        "row-7": 32
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
