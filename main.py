from Algorithm.history_manager import HistoryManager
from Algorithm.move_manager import MoveManager
from Algorithm.rules import Rules
from Algorithm.settings import Settings
from Algorithm.strategy_manager import StrategyManager


from ImageRecognition import image



def main():
    # Use a breakpoint in the code line below to debug your script.
    hm = HistoryManager(1)
    settings = Settings()
    rules = Rules()
    mm = MoveManager()
    sm = StrategyManager()

    hm.check_history()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
