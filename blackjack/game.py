from deck import Deck
from player import Player
from dealer import Dealer
from colorama import init, Fore, Back, Style
import time
import os


# Global Variables
dealer = Dealer()
player = Player()
deck = Deck().create_deck()  # Create the Deck that contain the 52 cards (deck is already shuffle)
game_running = True  # Flag to stop player choices while
choices = ['hit', 'stand', 'dd']  # Player choices NOTE: develop function SPLIT


# To clear screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to draw the table OJO pass variable to control when to show card 1 or not
def draw_statistics():
    # cls()
    print('\n')
    print(dealer.draw_dealer_info())
    print('+'*20)
    print(player)
    print('\n')


# Function to ask player for information
def ask_player_info():
    name = ''
    money = 0
    while name == '':
        name = input('Please enter your name: ')
    player.name = name

    while money == 0:
        try:
            money = int(input('Please enter how much do you want to start: '))
            player.money_amount = money
        except ValueError:
            print(Fore.RED + "Oops! That was no valid number. Try again...")
            print(Style.RESET_ALL)


# Function to ask player to BET
def ask_player_bet():
    while True:
        try:
            bet = int(input('Please enter how much do you want to BET: '))
            if bet > player.money_amount:
                print(Fore.RED + f'Oops! You have ${player.money_amount}, it is not enough to make that bet.')
                print(Style.RESET_ALL)
                continue
            else:
                player.bet(bet)
                break
        except ValueError:
            print(Fore.RED + "Oops!  That was no valid number.  Try again...")
            print(Style.RESET_ALL)


# Function to distribute cards
def distribute_cards(who):
    if who.update_card_values() + deck[0].value > 21:
        who.make_aces_value_one()
    if deck[0].face == 'A' and who.update_card_values() > 10:
        deck[0].value = 1

    who.cards.append(deck.pop(0))


# Function to ask Player for one choice
def ask_player_choice():
    print('Available choices "Hit", "Stand", "DD (Double Down)"')
    choice = ''
    while choice not in choices:
        choice = input('Enter a valid choice: ').lower()
    return choice


# Function to check if someone has BJ after distributed the two firth cards
def check_for_blackjack():
    if player.has_blackjack() and not dealer.has_blackjack():
        # Dealer pay to player 1,5 times player's bet
        player.money_amount += player.bet_box * 1.5

        # Then Bet Box start again
        player.bet_box = 0

        # show information
        print(dealer.draw_complete_dealer_info())
        print(player)

        print(f'Congratulations {player.name}, you won with BLACKJACK :)!!!')
        print(f'Now you have {player.money_amount}')
        return True
    elif player.has_blackjack() and dealer.has_blackjack():
        # Player does not loose their bet
        player.money_amount += player.bet_box

        # Then Bet Box start again
        player.bet_box = 0

        # show information
        print(dealer.draw_complete_dealer_info())
        print(player)
        print('Wow!!! both of you has BLACKJACK that is pretty unlikely.')
        return True


def ask_player_to_play_again():
    global game_running
    global deck

    # Initialize variables
    deck = Deck().create_deck()
    player.cards.clear()
    dealer.cards.clear()

    answer = ''
    while answer not in ['Y', 'N']:
        answer = input('Would you like to play again? Please enter "Y" or "N": ').upper()

    if answer == 'Y':
        game_running = True
        handle_game()
    else:
        exit()


def process_dealer_hitting_cards():
    global game_running
    # Start Dealer hitting card process
    while True:
        print('Giving one card to Dealer...')
        distribute_cards(dealer)
        time.sleep(1)

        # update statistics
        print(dealer.draw_complete_dealer_info())
        print(player)

        # check if dealer BURST
        if dealer.is_burst():
            # pay to player
            player.money_amount += player.bet_box*2
            player.bet_box = 0

            print(f'\nCongratulations {player.name}, you won this time (dealer BURST)')

            # show player their numbers alfter round
            print(f'\nPlayer {player.name} you have ${player.money_amount}.')

            game_running = False
            break
        elif dealer.update_card_values() > player.update_card_values():
            # Player loose their money and bet box starts again
            player.bet_box = 0

            print(f'\nOops!!! Dealer is closer to 21 than you. This time Dealer won.')

            # show player their numbers after round
            print(f'\nPlayer {player.name} you have ${player.money_amount}.')

            game_running = False
            break
        else:
            continue


# Function to manage game depending of the player's choice
def handle_game():
    global game_running

    # If player money is zero might be a new player
    if player.money_amount == 0:
            ask_player_info()

    # STEP 2 - Ask player to place a bet
    ask_player_bet()

    # STEP 3 - Distribute the first TWO cards to player and dealer (One time Player and one time Dealer)
    # NOTE put a time to simulate distributing first two cards
    print('Distributing cards......')
    distribute_cards(player)
    distribute_cards(dealer)
    distribute_cards(player)
    distribute_cards(dealer)
    time.sleep(2)

    # check if someone (or both) has BJ in the first two cards
    if check_for_blackjack():
        print('This round is over')
    else:
        while game_running:
            # Show statistics
            draw_statistics()

            # ask for a choice
            choice = ask_player_choice()

            if choice == 'hit':
                # give another card to player
                distribute_cards(player)
                print('Giving one card to player......')
                time.sleep(1)
                draw_statistics()  # To check

                # check if player BURST
                if player.is_burst():
                    # Player loose their money and bet box starts again
                    player.bet_box = 0

                    print(f'\nOops!!! {player.name}, you got BURST.')

                    # show player their numbers after round
                    print(f'\nPlayer {player.name} you have ${player.money_amount}.')
                    game_running = False
                    break

            if choice == 'stand':
                # show COMPLETE dealer info and start giving cards to dealer in case not BJ in place
                print(dealer.draw_complete_dealer_info())

                if dealer.has_blackjack():
                    # Player loose their money and bet box starts again
                    player.bet_box = 0

                    print(f'\nOops!!! Sorry {player.name} dealer got BlackJack.')

                    # show player their numbers after round
                    print(f'\nPlayer {player.name} you have ${player.money_amount}.')

                    game_running = False
                    break
                else:
                    process_dealer_hitting_cards()

            # check if player choose DD (Double Down)
            if choice == 'dd':
                if player.can_double_down():
                    # automatically double the bet amount
                    player.bet(player.bet_box)

                    # then give a third card to player
                    distribute_cards(player)
                    print('Giving one card to player......')
                    time.sleep(1)

                    # show info to check the bet box
                    draw_statistics()

                    if player.is_burst():
                        # Player loose their money and bet box starts again
                        player.bet_box = 0

                        print(f'\nOops!!! {player.name}, you got BURST.')

                        # show player their numbers after round
                        print(f'\nPlayer {player.name} you have ${player.money_amount}.')
                        game_running = False
                        break
                    else:
                        # show COMPLETE dealer info and start giving cards to dealer in case not BJ in place
                        print(dealer.draw_complete_dealer_info())

                        if dealer.has_blackjack():
                            # Player loose their money and bet box starts again
                            player.bet_box = 0

                            print(f'\nOops!!! Sorry {player.name} dealer got BlackJack.')

                            # show player their numbers after round
                            print(f'\nPlayer {player.name} you have ${player.money_amount}.')

                            game_running = False
                            break
                        else:
                            process_dealer_hitting_cards()
                else:
                    print('You do not have the requirements to DoubleDown.')
                    print('You must have a sum of 9, 10 , or 11 between your cards.')
                    print('Also you must have enough money to double your original bet.')

    # At the end of each round ask to play again
    ask_player_to_play_again()


'''GAME FLOW'''
# Say welcome
print(Fore.GREEN + 'Welcome to Blackjack a Las Vegas style!!!')
print(Style.RESET_ALL)

# STEP 1 - Call ask player for name and amount of money information
ask_player_info()

# THEN. Handle the game according player choices
handle_game()



