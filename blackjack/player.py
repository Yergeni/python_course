from colorama import init, Fore, Back, Style


class Player:

    def __init__(self, name='', cards=[], money_amount=0, bet_box=0, is_split=False):
        self.name = name
        self.cards = cards
        self.bet_box = bet_box
        self.money_amount = money_amount
        self.is_split = is_split

    def bet(self, amount):
        self.bet_box += amount
        self.money_amount -= amount

    # improve this for
    def update_card_values(self):
        value = 0
        for c in self.cards:
            value += c.value
        return value

    # Define if player can chose DoubleDown
    def can_double_down(self):
        # Player can only DD if sum of their first two card are between 9 and 11 and
        # of course has enough money to double the initial bet
        return 9 <= self.update_card_values() <= 11 and self.money_amount >= self.bet_box

    def is_burst(self):
        return self.update_card_values() > 21

    def has_blackjack(self):
        if self.update_card_values() == 21:
            return True

    # In case that an ace already given need to chance its value from 11 to 1
    def make_aces_value_one(self):
        for c in self.cards:
            if c.face == 'A':
                c.value = 1

    def __str__(self):
        draw = ''
        # value = 0
        print(f'PLAYER {self.name.upper()} INFORMATION')
        print('-'*20)
        draw += f'| MONEY: {self.money_amount}| BB: {self.bet_box} '

        for c in self.cards:
            # value += c.value
            draw += f'| {c.face}{c.suit} '
        draw += f'| Amount: {self.update_card_values()} |'

        return draw
