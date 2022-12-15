import random
import cv2
from keras.models import load_model
import numpy as np

print ('\nThis is a Rock-Paper-Scissors game!!\n')
choice_list = ['Rock', 'Paper','Scissors', 'Nothing']
print ('\nPlease, show a sign to the camera according to the list' + str(choice_list) + ': \n')

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
    
def get_prediction():
    '''
    The function takes user input and it returns.
    
    Variable:
    ---------
    user_input: str
        The word to be guessed as user input from the choice_list.
    
    Atributes:
    ----------
    choice_list: list
        List of choices to be used in the game.
    '''
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        max_index_prediction = np.argmax(prediction[0])
        user_input = choice_list[max_index_prediction]
        print (user_input)
        if cv2.waitKey(1) & 0xFF == ord ('q'):
            break
        
    cap.release() # After the loop release the cap object
    cv2.destroyAllWindows() # Destroy all the windows
    
    print ('User choice: ' + user_input)
    return user_input


def get_winner():
    '''
    The function to get a winner between "computer_choice" and "user_choice".
    
    If computer/user choice is Rock and user/computer choice is Scissors, Rock choice wins.
    Else, if computer/user choice is Paper and user/computer choice is Rock, Paper choice wins.
    Else, if computer/user choice is Scissors and user/computer choice is Paper, Scissors choice wins.
    Else, if computer/user choice is Nothing or user and computer choice is Nothing, continue playing the game.
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
    user_choice = get_prediction()
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
        
    elif computer_choice == "Nothing" and user_choice == "Nothing":
        print ('Please, try again.')
    
    elif computer_choice == "Nothing" or user_choice == "Nothing":
        print ('Please, try again.')
    
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