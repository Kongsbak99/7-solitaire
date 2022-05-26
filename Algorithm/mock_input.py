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
