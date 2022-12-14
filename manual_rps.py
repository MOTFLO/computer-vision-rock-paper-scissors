import random

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
    #print ('Computer choice is: ' + computer_choice)
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
    computer_choice = get_computer_choise()
    user_choice = get_user_choice()
    
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
    return

winner = get_winner()