from Algorithm.MainPlayFunctions.image_rec_confirmer import confirmCard
from Algorithm.MainPlayFunctions.mock_input import mockImageRec


def unknownCards(board):
    # Check row stacks
    # Row 1
    if board["row-stack"]["row-1"]:
        if board["row-stack"]["row-1"][0] == -1:
            rec_card = mockImageRec()
            actual_card = confirmCard(rec_card)
            board["row-stack"]["row-1"][0] = actual_card
            return board

    # Row 2
    if board["row-stack"]["row-2"]:
        if board["row-stack"]["row-2"][0] == -1:
            rec_card = mockImageRec()
            actual_card = confirmCard(rec_card)
            board["row-stack"]["row-2"][0] = actual_card
            return board

    # Row 3
    if board["row-stack"]["row-3"]:
        if board["row-stack"]["row-3"][0] == -1:
            rec_card = mockImageRec()
            actual_card = confirmCard(rec_card)
            board["row-stack"]["row-3"][0] = actual_card
            return board

    # Row 4
    if board["row-stack"]["row-4"]:
        if board["row-stack"]["row-4"][0] == -1:
            rec_card = mockImageRec()
            actual_card = confirmCard(rec_card)
            board["row-stack"]["row-4"][0] = actual_card
            return board

    # Row 5
    if board["row-stack"]["row-5"]:
        if board["row-stack"]["row-5"][0] == -1:
            rec_card = mockImageRec()
            actual_card = confirmCard(rec_card)
            board["row-stack"]["row-5"][0] = actual_card
            return board

    # Row 6
    if board["row-stack"]["row-6"]:
        if board["row-stack"]["row-6"][0] == -1:
            rec_card = mockImageRec()
            actual_card = confirmCard(rec_card)
            board["row-stack"]["row-6"][0] = actual_card
            return board

    # Row 7
    if board["row-stack"]["row-7"]:
        if board["row-stack"]["row-7"][0] == -1:
            rec_card = mockImageRec()
            actual_card = confirmCard(rec_card)
            board["row-stack"]["row-7"][0] = actual_card
            return board

    # Check wastepile
    if board["waste-pile"]:
        if board["waste-pile"][0] == -1:
            rec_card = mockImageRec()
            actual_card = confirmCard(rec_card)
            board["waste-pile"][0] = actual_card
            return board

    return board
