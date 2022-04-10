from Algorithm.cards import Cards
from Algorithm.history_manager import HistoryManager
from Algorithm.move_manager2 import MoveManager
from Algorithm.rules import Rules
from Algorithm.settings import Settings
from Algorithm.strategy_manager import StrategyManager


from ImageRecognition import image



def main():
    # Use a breakpoint in the code line below to debug your script.
    hm = HistoryManager()
    settings = Settings()
    rules = Rules()
    mm = MoveManager()
    sm = StrategyManager()

    # hm.check_history()

    MoveManager.movables()
    print(MoveManager.legal_moves)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
