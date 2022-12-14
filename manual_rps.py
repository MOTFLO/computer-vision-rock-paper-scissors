import random

print ('\nThis is a Rock, Paper and Scissors game!!\n')

choice_list = ['Rock', 'Paper','Scissors']

def get_computer_choise():
    '''
    The function picks randomly an option from the 'list_choice'.
    
    Variable:
    ---------
    computer_choice: str
        The word to be guessed piecked randomly from the choice_list.
    
    Atributes:
    ----------
    choice_list: list
        List of choices to be used in the game.
    '''
    
    computer_choice = random.choice(choice_list)
    print ('Computer choice is: ' + computer_choice)
    return computer_choice

def get_user_choice():
    '''
    The function takes user input and return it.
    
    Variable:
    ---------
    user_input: str
        The word to be guessed as user input from the choice_list.
    
    Atributes:
    ----------
    choice_list: list
        List of choices to be used in the game.
    '''
    user_input = input('Please, select a word from the list ' + str(choice_list) + ': ')
    user_input = user_input.capitalize()
    print ('User choice: ' + user_input)
    return user_input



def get_winner():
    '''
    The function to get a winner between "computer_choice" and "user_choice".
    
    If computer/user choice is Rock and user/computer choice is Scissors, Rock choice wins.
    Else, if computer/user choice is Paper and user/computer choice is Rock, Paper choice wins.
    Else, if computer/user choice is Scissors and user/computer choice is Paper, Scissors choice wins.
    Else, if computer choice is equal to user choice, then is a tie.
    
    Attributes:
    ----------
    computer_choice: str
        Is getting the computer random choice function.

    user_choice: str
        Is getting the user input function, manualy.

    Returns:
    -------
    get_winner:str
        Returns the winner of the game.
    '''
    user_choice = get_user_choice()
    computer_choice = get_computer_choise()
    
    if computer_choice == "Rock" and user_choice == "Scissors":
        print ('You lost!')
        
    elif computer_choice == "Paper" and user_choice == "Rock":
        print ('You lost.')
        
    elif computer_choice == "Scissors" and user_choice == "Paper":
        print ('You lost!')
    
    elif user_choice == "Paper" and computer_choice == "Rock":
        print ('You won!')
        
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print ('You won!')
        
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print ('You won!')
    
    elif computer_choice == user_choice:
        print ('It is a tie!')
    
    return get_winner()

def play():
    '''
    The play function, to get the winner of the game that is set to any.
    
    Variable:
    --------
    winner: Any
        It gets the winner of the game using "get_winner" function.
        
    Return:
    ------
    winner: Any
        Will return the winner of the game.
    '''
    winner = get_winner()
    return winner

play_game = play()