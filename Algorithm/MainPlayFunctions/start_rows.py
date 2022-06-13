from Algorithm.MainPlayFunctions.image_rec_confirmer import confirmCard
from Algorithm.MainPlayFunctions.mock_input import mockImageRec


def startRows(board):
    # Row-1
    recognized_card = mockImageRec()
    actual_card = confirmCard(recognized_card)
    board["row-stack"]["row-1"][0] = actual_card

    # Row-2
    recognized_card = mockImageRec()
    actual_card = confirmCard(recognized_card)
    board["row-stack"]["row-2"][0] = actual_card

    # Row-3
    recognized_card = mockImageRec()
    actual_card = confirmCard(recognized_card)
    board["row-stack"]["row-3"][0] = actual_card

    # Row-4
    recognized_card = mockImageRec()
    actual_card = confirmCard(recognized_card)
    board["row-stack"]["row-4"][0] = actual_card

    # Row-5
    recognized_card = mockImageRec()
    actual_card = confirmCard(recognized_card)
    board["row-stack"]["row-5"][0] = actual_card

    # Row-6
    recognized_card = mockImageRec()
    actual_card = confirmCard(recognized_card)
    board["row-stack"]["row-6"][0] = actual_card

    # Row-7
    recognized_card = mockImageRec()
    actual_card = confirmCard(recognized_card)
    board["row-stack"]["row-7"][0] = actual_card

    return board
