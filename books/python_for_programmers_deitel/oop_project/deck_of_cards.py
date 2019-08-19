import random
from card import Card


class DeckOfCards:
    NUMBER_OF_CARDS = 52

    def __init__(self):
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13], Card.SUITS[count // 13]))

    def shuffle(self):
        self._current_card = 0
        random.shuffle(self._deck)

    def deal_card(self):
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except:
            return None

    def __str__(self):
        output = ""
        for index, card in enumerate(self._deck):
            output += f"{str(card):>20}"
            if (index + 1) % 4 == 0:
                output += "\n"

        return output

if __name__ == "__main__":
    deck_of_cards = DeckOfCards()

    print(deck_of_cards)
    print(deck_of_cards.deal_card())

    deck_of_cards.shuffle()
    print(deck_of_cards)
