from image_rec_confirmer import confirmCard
from mock_input import mockImageRec




def unknownCards(board):
    mock_input = {
        "waste-pile": board['waste-pile'],
        "row-stack": board['row-stack']
    }
    if mock_input['waste-pile']:
        if mock_input['waste-pile'][0] == -1:
            rec_card = mockImageRec()
            actual_card = confirmCard(rec_card)
            mock_input['waste-pile'] = actual_card
    for row in mock_input['row-stack']:
        if mock_input['row-stack'][row][0] == -1:
            rec_card = mockImageRec()
            actual_card = confirmCard(rec_card)
            mock_input['row-stack'][row][0] = actual_card
    
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

    return board
