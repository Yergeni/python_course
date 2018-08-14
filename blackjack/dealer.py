

class Dealer:

    def __init__(self, cards=[]):
        self.cards = cards

    #  make better and short
    def update_card_values(self):
        value = 0
        # value += [c.value for c in self.cards]
        for c in self.cards:
            value += c.value
        return value

    def is_burst(self):
        return self.update_card_values() > 21

    def has_blackjack(self):
        return self.update_card_values() == 21

    # In case that an ace already given need to chance its value from 11 to 1
    def make_aces_value_one(self):
        for c in self.cards:
            if c.face == 'A':
                c.value = 1

    def draw_complete_dealer_info(self):
        draw = ''
        # value = 0
        print('\n')
        print('DEALER INFORMATION')
        print('-'*20)

        for c in self.cards:
                # value += c.value
                draw += f'| {c.face}{c.suit} '

        draw += f'| Amount: {self.update_card_values()} |'

        return draw

    def draw_dealer_info(self):
        draw = ''
        value = 0
        print('DEALER INFORMATION')
        print('-'*20)
        draw += '| Hidden CARD '

        for c in self.cards[1:]:
                value += c.value
                draw += f'| {c.face}{c.suit} '

        return draw
