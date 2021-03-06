import json

from Algorithm.cardss import Cardss


class StrategyManager:

    def __init__(self, moves):
        self.moves = moves

        with open('board.json') as f:
            self.board = json.load(f)

    # main method for general flow of strategy manager

    def best_move(self):
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 4 or self.moves[i]['moveType'] == 1:
                best_moves = self.moves[i]
                return best_moves
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 5:
                best_moves = self.moves[i]
                return best_moves
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 3:
                best_moves = self.moves[i]
                return best_moves
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 6:
                best_moves = self.moves[i]
                return best_moves
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 2:
                best_moves = self.moves[i]
                return best_moves
        for i in range(len(self.moves)):
            if self.moves[i]['moveType'] == 7:
                best_moves = self.moves[i]
                return best_moves

    # def best_move(self):
    #     moves = []
    #     # Check for suit move
    #     for i in range(len(self.moves)):
    #         if self.moves[i]['moveType'] == 4 or self.moves[i]['moveType'] == 1:
    #             moves.append(self.moves[i])
    #     if len(moves) > 0:
    #         best_move = self.suit_stack_move(moves)
    #         if best_move == 'skip':
    #             moves = []
    #         else: return best_move
    #     # Check for king row move
    #     for i in range(len(self.moves)):
    #         if self.moves[i]['moveType'] == 5:
    #             moves.append(self.moves[i])
    #     if len(moves) > 0:
    #         best_move = self.king_move(moves)
    #         if best_move == 'skip':
    #             moves = []
    #         else: return best_move
    #     # Check for row move
    #     for i in range(len(self.moves)):
    #         if self.moves[i]['moveType'] == 3:
    #             moves.append(self.moves[i])
    #     if len(moves) > 0:
    #         best_move = self.row_stack_move(moves)
    #         if best_move == 'skip':
    #             moves = []
    #         else: return best_move
    #
    #     # Check for king waste move
    #     for i in range(len(self.moves)):
    #         if self.moves[i]['moveType'] == 6:
    #             moves.append(self.moves[i])
    #     if len(moves) > 0:
    #         best_move = self.king_move(moves)
    #         return best_move
    #
    #     # Check for waste row move
    #     for i in range(len(self.moves)):
    #         if self.moves[i]['moveType'] == 2:
    #             moves.append(self.moves[i])
    #     if len(moves) > 0:
    #         best_move = self.row_stack_move(moves)
    #         return best_move
    #
    #     # Turn stockpile move
    #     for i in range(len(self.moves)):
    #         if self.moves[i]['moveType'] == 7:
    #             moves.append(self.moves[i])
    #     if len(moves) > 0:
    #         best_move = self.no_moves(moves)
    #         return best_move

    def suit_stack_move(self, moves):

        for move in moves:
            card = move['cards'][0]
            move_card = Cardss.getCardValue(card)

            # Do not make waste to suit stack move, if it will make the stock+waste pile % 3 = 0 because then it locks the pile
            if move['moveType'] == 1:
                stock_pile = self.board['stock-pile']
                waste_pile = self.board['waste-pile']
                test = (len(stock_pile)+len(waste_pile)-1) % 3
                if ((len(stock_pile)+len(waste_pile))-1) % 3 == 1 or ((len(stock_pile)+len(waste_pile))-1) % 3 == 2:
                    return move
                if ((len(stock_pile)+len(waste_pile))-1) % 3 == 0:
                    continue # So if making the move would lock the pile, continue (skip this move)

            if card == 1 or card == 14 or card == 27 or card == 40 or card == 2 or card == 15 or card == 28 or card == 41:
                return move

            else:
                board = self.board
                count = 0
                for row in board['row-stack']:
                    if len(board['row-stack'][row]) > 0:
                        row_card = Cardss.getCardValue(board['row-stack'][row][0])
                        for card in board['row-stack'][row]:
                            if card != 0:
                                row_card = Cardss.getCardValue(card)
                                if row_card == move_card-2:
                                    count = count + 1
                for stack in board['suit-stack']:
                    if len(board['suit-stack'][stack]) > 1:
                        for card in range(len(board['suit-stack'][stack])):
                            if card != 0:
                                suit_card = Cardss.getCardValue(board['suit-stack'][stack][card])
                                if suit_card == move_card-2:
                                    count = count + 1
                if count == 4:
                    return move
        return 'skip'

    def king_move(self, moves):

        # If stock pile % 3 == 0, we choose the waste pile move, to make sure the stock pile doesnt get locked.
        for move in moves:
            if move['moveType'] == 6:
                stock_pile = self.board['stock-pile']
                waste_pile = self.board['waste-pile']
                if (len(stock_pile)+len(waste_pile)) % 3 == 0:
                    return move

        if len(moves) == 1 and moves[0]['moveType'] == 6:
            return moves[0]
        # Else we consider the rest of the possible king moves
        # If more than one king move, we choose the one moving from a pile with more unknown cards.
        #if len(moves) > 1:
        rows = [] # Rows moves are moved from
        for row in self.board['row-stack']:
            for move in moves:
                if self.board['row-stack'][row]:
                    # Check that it is a row (not waste pile)
                    if self.board['row-stack'][row][0] == move['cards'][0]:
                        total_length = len(self.board['row-stack'][row])
                        move_type = move['moveType']
                        unknown_size = 0
                        for card in self.board['row-stack'][row]:
                            if card == 0:
                                unknown_size = unknown_size + 1
                        rows.append({'moved_from': row, 'moveId': move['moveId'], 'move_type': move_type, 'unknown_size': unknown_size, 'total_length': total_length})
        # Best move = the move with the most unknowns underneath.
        best_move = rows[0]
        for row in rows:
            if row['unknown_size'] != 0:
                best_move = row
        for row in rows:
            if row['unknown_size'] < best_move['unknown_size'] and row['unknown_size'] != 0:
                best_move = row
        if best_move['move_type'] == 5 and best_move['unknown_size'] == 0:
            return 'skip'
        else:
            for move in moves:
                if move['moveId'] == best_move['moveId']:
                    return move

    def row_stack_move(self, moves):
        # Check if only move is movetype  2
        movetype_3_found = False
        for move in moves:
            if move['moveType'] == 3:
                movetype_3_found = True
        if movetype_3_found == False: return moves[0]

        # Check if a King is available
        king_available = False
        for row in self.board['row-stack']:
            if self.board['row-stack'][row]:
                for card in self.board['row-stack'][row]:
                    if self.board['row-stack'][row][len(self.board['row-stack'][row])-1] != 0:
                        king_available = False
                    elif (card == 13 or card == 26 or card == 39 or card == 52) and len(self.board['row-stack'][row]) > 1:
                        king_available = True
        if self.board["waste-pile"]:
            if self.board['waste-pile'][0] == 13 or self.board['waste-pile'][0] == 26 or self.board['waste-pile'][0] == 39 or self.board['waste-pile'][0] == 52:
                king_available = True

        rows = [] # Rows moves are moved from
        for row in self.board['row-stack']:
            for move in moves:
                if self.board["row-stack"][row]:
                    if self.board['row-stack'][row][0] == move['cards'][0]:
                        total_length = len(self.board['row-stack'][row])
                        unknown_size = 0
                        for card in self.board['row-stack'][row]:
                            if card == 0:
                                unknown_size = unknown_size + 1
                        rows.append({'moved_from': row, 'moveId': move['moveId'], 'unknown_size': unknown_size, 'total_length': total_length})

        best_move = rows[0]
        if king_available == True:
            # Check which row is the smallest
            for row in rows:
                if row['total_length'] < best_move['total_length']:
                    best_move = row
        else:
            # Check which row has the most 0'
            for row in rows:
                if row['unknown_size'] > best_move['unknown_size']:
                    best_move = row

        if best_move['unknown_size'] == 0 and king_available == False:
            return 'skip'
        else:
            # Find the best move and return
            for move in moves:
                if move['moveId'] == best_move['moveId']:
                    return move

    # This function can probably be ignored
    def no_moves(self, moves):
        return moves[0]
