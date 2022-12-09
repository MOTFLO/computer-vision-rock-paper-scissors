import random

choice_list = ['rock', 'paper','scissors']
computer_choice = random.choice(choice_list)

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
    pass

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
    print ('User choice: ' + user_input)
    pass

computer_choice = get_computer_choise()
user_choice = get_user_choice()