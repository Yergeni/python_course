from card import Card
from random import shuffle


class Deck:

    def __init__(self, amount=1):
        self.amount = amount

    def create_deck(self):
        suits = {'♣', '♦', '♥', '♠'}
        faces = {'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
        cards = list()

        for s in suits:
            for f in faces:
                if f == 'A':
                    v = 11
                elif f == 'J' or f == 'Q' or f == 'K':
                    v = 10
                else:
                    v = f

                card = Card(s, f, v)
                cards.append(card)
                shuffle(cards)

        return cards



