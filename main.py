# #from Algorithm.MainPlayFunctions.image_rec_confirmer import confirmCard
# import time
#
#
# from Algorithm.OldMainPlayFunctions.new_look_for_unkown_cards import unknownCards
# #from Algorithm.MainPlayFunctions.mock_input import mockImageRec
# #from Algorithm.MainPlayFunctions.play_loop import playLoop
# from Algorithm.cardss import Cardss
# from Algorithm.history_manager import HistoryManager
# from Algorithm.OldMainPlayFunctions.old_mock_input import init_mock_input
# from Algorithm.move_manager import MoveManager
# from Algorithm.strategy_manager import StrategyManager
#
# from Algorithm.PlayLoopFunctions.image_rec_confirmer import confirmCard
# from Algorithm.PlayLoopFunctions.mock_input import mockImageRec
#
# from Algorithm.MoveTypes.turn_stockpile import turnStockpile
# from Algorithm.PlayLoopFunctions.mock_input import imgrec_service, mock, mockImageRec
#
#
# import json
#
# from ImageRecognition.run import runAllCards
#
#
# #await runAllCards(cap)
# from ImageRecognition.runrun import getCap, runmycards
#
#
# def main():
#
#
#     print("IVE BEEN RUN")
#     ##initiate start game
#     game_end = False
#
#     #TODO fjern init_input her:
#     # init_input = init_mock_input()
#     print("Best move is turning the stockpile ONCE")
#     confirmer = input()
#
#     #TODO Fjern hashtag på de 2 linjer under og ændre imgrec_input = deres imgrec metode
#     imgrec_input = runAllCards(cap) # TODO i stedet for imgrec_metode(), deres imgrec metode metode
#     time.sleep(1)
#     init_input = imgrec_service(imgrec_input)
#     hm = HistoryManager(init_input)  ##init game
#     with open('board.json') as f:
#         board = json.load(f)
#         f.close()
#     f.close()
#
#     prev_moves = []
#     #### General flow of game
#     while game_end == False:  ##Keep while loop active, until game is finished.
#         ##TODO: Check for lost game
#
#         mm = MoveManager()
#         ##After init of board, check for moves
#         mm.movables()
#         legal_moves = mm.legal_moves
#         print(f"Possible moves in Main: {legal_moves}")
#         print("")
#
#         if len(prev_moves) > 0:
#             removed = []
#             for legal_move in legal_moves:
#                 count = 0
#                 if 'cards' in legal_move:
#                     for move in prev_moves:
#                         if legal_move['to'] == move['to'] and legal_move['cards'] == move['cards']:
#                             count = count + 1
#                 if count > 1:
#                     removed.append(legal_move)
#             for move in removed:
#                 legal_moves.remove(move)
#
#         ##Init Strategy Manager and pass legal moves from Move Manager
#         sm = StrategyManager(legal_moves)
#         # Check the best move
#         if sm.best_move()["moveType"] == 7:
#             print("Best move is turning the stockpile ONCE")
#         else:
#             best_move = sm.best_move()
#             cards = best_move["cards"]
#             cards_name = []
#             for card in cards:
#                 cards_name.append(Cardss.getCardName(card))
#             location = sm.best_move()["to"]
#             print("Best move is moving card(s): " + str(cards_name) + ", to " + str(location))
#
#         print("Confirm that move is performed with ENTER")
#         input_confirmer = input()
#         ##Make move
#         board_after_move = mm.doMove(sm.best_move())  ##complete board
#         print("Board after move")
#         ##Finally update board to new state
#         new_input = hm.update_board(board_after_move)
#         print("Board after update")
#
#         # Check for victory
#         game_end = hm.check_for_victory()
#
#         prev_moves.append(best_move)
#
#
#         print("###################################")
#     print("Game ended")
#
# cap = getCap()
# if __name__ == '__main__':
#     main()
#     #runmycards(cap)
#     #time.sleep(25)
