from Algorithms import foundationPile, regularPile
from ImageRecognition import image, video

def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    fill_foundation_pile = foundationPile.checkFoundationPile()
    move_regular_piles = regularPile.checkRegularPile()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
