from random import shuffle
from card import Card


def create_cards():
    suits = {'clubs', 'diamonds', 'hearts', 'spades'}
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
            # shuffle(cards)
    return cards


for c in create_cards():
    s,f,v = (c.suit, c.face, c.value)
    print(s,f,v)
