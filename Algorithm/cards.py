class Card:
    def __init__(self, card_id, suit, value):
        self.card_id = card_id
        self.suit = suit
        self.value = value


class Cards:
    sa = Card(1, 1, 1)
    s2 = Card(2, 1, 2)
    s3 = Card(3, 1, 3)
    s4 = Card(4, 1, 4)
    s5 = Card(5, 1, 5)
    s6 = Card(6, 1, 6)
    s7 = Card(7, 1, 7)
    s8 = Card(8, 1, 8)
    s9 = Card(9, 1, 9)
    s10 = Card(10, 1, 10)
    sj = Card(11, 1, 11)
    sq = Card(12, 1, 12)
    sk = Card(13, 1, 13)

    ca = Card(14, 2, 1)
    c2 = Card(15, 2, 2)
    c3 = Card(16, 2, 3)
    c4 = Card(17, 2, 4)
    c5 = Card(18, 2, 5)
    c6 = Card(19, 2, 6)
    c7 = Card(20, 2, 7)
    c8 = Card(21, 2, 8)
    c9 = Card(22, 2, 9)
    c10 = Card(23, 2, 10)
    cj = Card(24, 2, 11)
    cq = Card(25, 2, 12)
    ck = Card(26, 2, 13)

    ha = Card(27, 3, 1)
    h2 = Card(28, 3, 2)
    h3 = Card(29, 3, 3)
    h4 = Card(30, 3, 4)
    h5 = Card(31, 3, 5)
    h6 = Card(32, 3, 6)
    h7 = Card(33, 3, 7)
    h8 = Card(34, 3, 8)
    h9 = Card(35, 3, 9)
    h10 = Card(36, 3, 10)
    hj = Card(37, 3, 11)
    hq = Card(38, 3, 12)
    hk = Card(39, 3, 13)

    da = Card(40, 4, 1)
    d2 = Card(41, 4, 2)
    d3 = Card(42, 4, 3)
    d4 = Card(43, 4, 4)
    d5 = Card(44, 4, 5)
    d6 = Card(45, 4, 6)
    d7 = Card(46, 4, 7)
    d8 = Card(47, 4, 8)
    d9 = Card(48, 4, 9)
    d10 = Card(49, 4, 10)
    dj = Card(50, 4, 11)
    dq = Card(51, 4, 12)
    dk = Card(52, 4, 13)

    card_array = [
        sa, s2, s3, s4, s5, s6, s7, s8, s9, s10, sj, sq, sk,
        ca, c2, c3, c4, c5, c6, c7, c8, c9, c10, cj, cq, ck,
        ha, h2, h3, h4, h5, h6, h7, h8, h9, h10, hj, hq, hk,
        da, d2, d3, d4, d5, d6, d7, d8, d9, d10, dj, dq, dk
    ]

    def getCardSuit(card_id):
        for card in Cards.card_array:
            if card.card_id == card_id:
                print("card suit: " + card.suit)
                return card.suit

    def getCardValue(card_id):
        for card in Cards.card_array:
            if card.card_id == card_id:
                print("card value: " + card.value)
                return card.value

    # Small method to get name of a card by id
    def getCardName(card_id):
        card_value = Cards.getCardValue(card_id)
        card_suit = Cards.getCardSuit(card_id)
        card_value_string = ""
        card_suit_string = ""

        if card_suit == 1:
            card_suit_string = "Spades"
        if card_suit == 2:
            card_suit_string = "Clubs"
        if card_suit == 3:
            card_suit_string = "Hearts"
        if card_suit == 4:
            card_suit_string = "Diamonds"

        if (card_value >= 2) and (card_value <= 10):
            card_value_string = str(card_value)
        if card_value == 1:
            card_value_string = "Ace"
        if card_value == 11:
            card_value_string = "Jack"
        if card_value == 12:
            card_value_string = "Queen"
        if card_value == 13:
            card_value_string = "King"

        card_name = card_value_string + " of " + card_suit_string
        print("card name: " + card_name)
        return card_name
