import cv2
import time
import random
import numpy as np
from keras.models import load_model

time.time()
choice_list = ['Rock', 'Paper','Scissors', 'Nothing']

def countdown_timer(t):
    '''
    The countdown timer function for the game.
    
    Variables:
    ---------
    min, sec: Any
        Calculates the number of minutes in a seconds using the "divmod()" function.
    
    timer: LiteralString
        Prints the minutes and seconds on the screen using the variable "time.format".
    
    Parameters:
    ----------
    t: Any
        Alocated number in seconds to countdown timer.

    Return:
    -------
    countdown_timer: Any
        Returns the countdown time in minutes and seconds.
    '''
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    return countdown_timer

def get_computer_choise():
    '''
    The function picks randomly an option from the "choice_list".
    
    Variables:
    ---------
    computer_choice: str
        The word to be guessed piecked randomly from the "choice_list".
    
    Atributes:
    ----------
    choice_list: list
        List of choices to be used in the game.
    
    Return:
    -------
    computer_choice: str
        Returns the random word from the "choice_list" as a string.
    '''
    computer_choice = random.choice(choice_list)
    print ('Computer choice is: ' + computer_choice)
    return computer_choice
    
def get_prediction():
    '''
    The function predicts the winner between "computer_choice" and "user_choice".
    
    If computer/user choice is Rock and user/computer choice is Scissors, Rock choice wins the round.
    Else, if computer/user choice is Paper and user/computer choice is Rock, Paper choice wins the round.
    Else, if computer/user choice is Scissors and user/computer choice is Paper, Scissors choice wins round.
    Else, if computer/user choice is Nothing or user and computer choice is Nothing, continue playing the game.
    Else, if computer choice is equal to user choice, then is a round tie.
    Else, If computer/user wins 3 times in a row, user/computer wins the game.
    Else, If computer equals to user wins 3 times in a row, it is a game tie.
    
    Variables:
    ----------
    t: Literal
        Allocated time in seconds.
        
    countdown_timer: Any
        The function is counting the time at starting point of the game.
        
    choice_list: list[str]
        A defined list of words for R-P-S game.
    
    model: Any
        Loading the Computer Vision model.
        
    cap: Any
        The Video Capture.
        
    data: ndarray
        Collection of items of the same type.
        
    computer_wins: Literal[0]
        Normalization of the variable.
        
    user_wins: Literal[0]
        Normalization of the variable.
        
    number_rounds: Literal[0]
        Normalization of the variable.
        
    ret, frame: Any
        Is a boolean regarding whether or not there was a return at all, at the frame is each frame that is returned.
        
    resized_frame: Mat
        Resizing, by default, does only change the width and height of the image.
        
    normalized_image: NDArray[floating]
        Normalizing the image.
        
    prediction: Any
        Given a trained model, predict the label of a new set of data.
        
    max_index_prediction: intp
        Returns indices of the max element of the prediction array in axis [0].
        
    user_choice: str
        Assigns the user highest prediction shwon to the camera, from "max_index_prediction" to the corresponding name in "choice_list".
        
    computer_choice: str
        Is getting the computer random choice function.

    Return:
    -------
    get_prediction: str
        Returns the predicted winner of the game.
    
    '''
    print ('\nThis is a Rock-Paper-Scissors game!!')
    print (f'\nPlease, show an option to the camera in:\n')
    t = 5
    countdown_timer(int(t))
    
    model = load_model('keras_model.h5', compile = False)
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    computer_wins = 0
    user_wins = 0
    number_rounds = 0
    print (f'\n=====================WELCOME TO R-P-S GAME!=====================')
    
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1
        
        while computer_wins < 3 and computer_wins >= 0 or user_wins < 3 and user_wins >= 0:
            
            number_rounds += 1
            print (f'\nThis is round number: {number_rounds}\n')
            
            data[0] = normalized_image
            prediction = model.predict(data)
            max_index_prediction = np.argmax(prediction[0])
            user_choice = choice_list[max_index_prediction]
            print(f'{user_choice}\n')

            computer_choice = get_computer_choise()
            
            if computer_choice == "Rock" and user_choice == "Scissors" or computer_choice == "Paper" and user_choice == "Rock" or computer_choice == "Scissors" and user_choice == "Paper":
                print (f'User choice: {user_choice}')
                print ('You lost!')
                computer_wins += 1
                user_wins -= 1
                if computer_wins == 3 and user_wins < 3:
                    print (f'\nComputer has won {computer_wins} times in a row. You lost the game.\n')
                    print (f'******************************R-P-S******************************\n')
                    print (f'Press the letter "q" on your keyboard to close the window.\n')
                    break
                
                elif computer_wins == 3 and user_wins == 3:
                    print (f'\nNo one has won the game. It is a tie!\n')
                    break
                
            elif user_choice == "Paper" and computer_choice == "Rock" or user_choice == "Rock" and computer_choice == "Scissors" or user_choice == "Scissors" and computer_choice == "Paper":
                print (f'User choice: {user_choice}')
                print ('You won!')
                computer_wins -= 1
                user_wins += 1
                if user_wins == 3 and computer_wins < 3:
                    print (f'\nYou have won {user_wins} times in a row. Congratulations, you won the game!\n')
                    print (f'******************************R-P-S******************************\n')
                    print (f'Press the letter "q" on your keyboard to close the window.\n')
                    break
                
                elif computer_wins == 3 and user_wins == 3:
                    print (f'\nNo one has won the game. It is a tie!\n')
                    break
     
            elif computer_choice == "Nothing" and user_choice == "Nothing":
                print (f'User choice: {user_choice}')
                print (f'\nNo one has won this round. Please, continue playing.\n')
    
            elif computer_choice == "Nothing" or user_choice == "Nothing":
                print (f'User choice: {user_choice}')
                print (f'\nNo one has won this round. Please, continue playing.\n')
                
            elif computer_choice == user_choice:
                print (f'User choice: {user_choice}')
                print (f'\nIt is a round tie! Please, continue playing.\n')
            
            print (f'\n******************************R-P-S******************************')
            break
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(1000) & 0xFF == ord('q'): # Press "q" to close the window
            break
    cap.release() # After the loop release the cap object
    cv2.destroyAllWindows() # Destroy all the windows
    return get_prediction

def play():
    '''
    The play function, to get the winner of the game that is set to any.
    
    If the input from "user_input" variable is "Yes" continue playing the R-P-S game, continue the while loop.
    Else, if the input from "user_input" variable is "No" print the messages and end the while loop.
    
    Variables:
    ---------
    winner: Any
        It gets the winner of the game using "get_predinction" function.
        
    user_input: str
        It takes an input from the user as string.
        
    Return:
    -------
    winner: Any
        Returns the winner of the game.
    '''
    winner = get_prediction()
    
    while True:
        user_input = input(f'Would you like to continue playing (Yes/No)?:')
        if user_input == 'Yes' or user_input == 'YES' or user_input == 'yes' or user_input == 'Y' or user_input == 'y':
            winner = get_prediction()
        elif user_input == 'No' or user_input == 'NO' or user_input == 'no' or user_input == 'N' or user_input == 'n':
            print(f'\nThank you for playing the R-P-S game!\n')
            print (f'========================SEE YOU NEXT TIME========================\n')
            exit()
        return winner

'''
Instantiating the "play()" class. 
'''
play_game = play()