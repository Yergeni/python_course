
# coding: utf-8

# In[13]:


# to clear the board
from IPython.display import clear_output

ref_board = ['#','1','2','3','4','5','6','7','8','9']
main_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
ref_options = list(range(1,10))
ref_winner_x = ['X']*3
ref_winner_o = ['O']*3
p1_mark = ''
p2_mark = ''

# print a main_board
def display_board_info(board):
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print("-----------")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("-----------")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    
# print a main_board
def display_board(board):
    clear_output()
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print("-----------")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("-----------")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")


# In[2]:


def clear_board(board):
    for pos in range(1,10):
        board[pos] = ' '


# In[3]:


def player1_mark():
    options = ['X', 'O']
    p1_mark = input('Player ONE please enter X or O: ').upper()
    
    while p1_mark not in options:
        p1_mark = input('Please enter a valid option (X or O): ').upper()
        
    return p1_mark


# In[4]:


def player2_mark(p1_mark):
    p2_mark = ''
    if p1_mark == 'X':
        p2_mark = 'O'
    else:
        p2_mark = 'X'
        
    return p2_mark


# In[14]:


def game_info():
    # Let players know their marks
    print('Welcome to Tic Tac Toe')
    print(f'Player ONE will be playing with {p1_mark} and Player TWO with {p2_mark}')
    
    # Show them the board as a reference
    print('\nHere you have a REFERENCE BOARD where the numbers corresponds to the positions.\n')
    display_board_info(ref_board)
    print('\n')


# In[6]:


# game_info()


# In[7]:


def player1_input():
    # Ask Player1 for his/her move and show the board updated
    p1 = 0
    
    # Validate input (verify vs strings)
    while p1 not in ref_options:
        p1 = int(input('Player ONE turn. Please enter a valid option between 1-9: '))
    
    while main_board[p1] != ' ':
        p1 = int(input('This position is already taken. Please enter a new position: '))
    
    return p1


# In[8]:


def player2_input():
    # Ask Player2 for his/her move and show the board updated
    p2 = 0
    
    # Validate input (verify vs strings)
    while p2 not in ref_options:
        p2 = int(input('Player TWO turn. Please enter a valid option between 1-9: '))
    
    while main_board[p2] != ' ':
        p2 = int(input('This position is already taken. Please enter a new position: '))
    
    return p2


# In[9]:


# Check winner and return a flag to compare later
def check_winner(board, ref_o, ref_x, p1_mark, p2_mark):
    win = 0
    rows = [board[1:4], board[4:7], board[7:], board[1:8:3], board[2:9:3], board[3::3], board[1::4], board[3:8:2]]
    for row in rows:
        if row == ref_x and p1_mark in ref_x or row == ref_o and p1_mark in ref_o:
            win += 1
        elif row == ref_x and p2_mark in ref_x or row == ref_o and p2_mark in ref_o:
            win += 2
            
    return win


# In[10]:


# Asking if players want to start again
def play_again(tie, win):
    if tie or win:
        play_again = ''
        while play_again not in ['Y','N']:
            play_again = input('Would you like to play again? (Type "Y" or "N"): ').upper()
            if play_again == 'Y':
                game()
            else:
                return 'Game ended. :('


# In[17]:


def game():
    # clear board before game start
    clear_board(main_board)
    game_info()

    # get input marks from players and save it GOLBALLY
    p1_mark = player1_mark()
    p2_mark = player2_mark(p1_mark)
    
    
    # flag to check if there is a winner
    won = False
    # flag to check if game finished tie   
    tied = False
    
    # loop to control the movements
    for move in range(1,5):
        # show some helpfull info
        
        print(f'\nStage No. {move}')
        # ask for player 1 move
        p1 = player1_input()
        # assign the position in board
        main_board[p1] = p1_mark
        # show the position in board
        display_board(main_board)
        
        #check for winner after every move and send message if one of the players won
        if check_winner(main_board, ref_winner_o, ref_winner_x, p1_mark, p2_mark) == 1:
            won = True
            print('CONGRATULATIONS!!! Player ONE won...')
            break
        elif check_winner(main_board, ref_winner_o, ref_winner_x, p1_mark, p2_mark) == 2:
            won = True
            print('CONGRATULATIONS!!! Player TWO won...')
            break
        
        print(f'\nStage No. {move}')
        p2 = player2_input()
        main_board[p2] = p2_mark
        display_board(main_board)
    
        #check for winner after every move and send message if one of the players won
        if check_winner(main_board, ref_winner_o, ref_winner_x, p1_mark, p2_mark) == 1:
            won = True
            print('CONGRATULATIONS!!! Player ONE won...')
            break
        elif check_winner(main_board, ref_winner_o, ref_winner_x, p1_mark, p2_mark) == 2:
            won = True
            print('CONGRATULATIONS!!! Player TWO won...')
            break
            
#         clear_output()
        
        
    # last move belogns to player1 in case not winner at this point
    if not won:
        print(f'\nStage No. {move}')
        p1 = player1_input()
        main_board[p1] = p1_mark
        display_board(main_board)

        #check for winner after every move and send message if one of the players won
        if check_winner(main_board, ref_winner_o, ref_winner_x, p1_mark, p2_mark) == 1:
            won = True
            print('CONGRATULATIONS!!! Player ONE won...')
        elif check_winner(main_board, ref_winner_o, ref_winner_x, p1_mark, p2_mark) == 2:
            won = True
            print('CONGRATULATIONS!!! Player TWO won...')
        else:
            print('Math TIED!!!')
            tied = True
    
    # Ask to start a new game if game was tied
    play_again(tied, won)
    


# In[18]:


game()

