import cv2
import random
import numpy as np
from datetime import datetime
from keras.models import load_model

class RPS:
    
    choice_list = ['Rock', 'Paper','Scissors', 'Nothing']
    
    def __init__(self):
        '''
        The initialization of the RPS class.
        
        Variables:
        ----------
        self.choice_list: str
            A deffined list of words for the game.
        '''
        self.choice_list = ['Rock', 'Paper','Scissors', 'Nothing']

    def get_computer_choise(self):
        '''
        The function picks randomly an option from the "self.choice_list".
        
        Variables:
        ---------
        computer_choice: str
            The word to be guessed piecked randomly from the "self.choice_list".
        
        Parameters:
        ----------
        self.choice_list: list[str]
            List of choices to be used in the game.
        
        Returns:
        -------
        computer_choice: str
            Returns the random word from the "self.choice_list" as a string.
        '''
        computer_choice = random.choice(self.choice_list)
        print ('Computer choice is: ' + computer_choice)
        return computer_choice
    
    def get_prediction(self):
        '''
        The function predicts the winner between "computer_choice" and "user_choice".
        
        While the sequences of statements are true and if keyboard pressed is number 13 start countdown the time. When countdown time is zero, start playing the game.
        Else, if keyboard pressed is "s" stop running the game and reset the game.
        Else, if keyboard pressed is "q" close the window and quit the game. After the loop release the cap object and destroy all windows.
        Else, if computer/user choice is Rock and user/computer choice is Scissors, Rock choice wins the round.
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
            Loads the Computer Vision model from "keras_model.h5".
            
        cap: Any
            The Video Capture.
            
        data: ndarray
            Collection items of the same type.
            
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
            Assigns the user highest prediction shwon to the camera, from "max_index_prediction" to the corresponding name in "self.choice_list".
            
        computer_choice: str
            Is getting the computer random choice from "get_computer_choice" function.
        
        font_1, font_2: int
            It denotes the font type for the text.
            
        start, quit, stop: str
            Variables to display the functionality for eack "key".
            
        frame: Any
            Displaying the frame content.
            
        key: Any
            The keyboard that is set to have a specific functionality.
            
        start_time: int
            Variable to get the current date and time, using the datetime class of the datetime module.
            
        diff_time: int
            Getting the current date and time in seconds.

        Returns:
        -------
        self.get_prediction: str
            Returns the predicted winner of the game as a string.
        
        '''
        model = load_model('keras_model.h5', compile = False)
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        
        while True:
            t = 5
            user_wins = 0
            computer_wins = 0
            number_rounds = 0
            
            ret, frame = cap.read()
            font_1 = cv2.FONT_HERSHEY_TRIPLEX
            font_2 = cv2.FONT_HERSHEY_PLAIN
            start = str('WELCOME TO R-P-S GAME!')
            quit = str('Quit => Q')
            stop = str('Stop => S')
            start_c = str('Start || Continue => ENTER')
            frame = cv2.putText(frame, str(datetime.now()), (10, 30), font_2, 1, (80, 255, 255), 2, cv2.LINE_AA) 
            frame = cv2.putText(frame, start, (90, 180), font_1, 1, (180, 255, 180), 2, cv2.LINE_AA)
            frame = cv2.putText(frame, quit, (10, 430), font_2, 1, (80, 255, 255), 2, cv2.LINE_AA)
            frame = cv2.putText(frame, start_c, (10, 460), font_2, 1, (80, 255, 255), 2, cv2.LINE_AA)
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            cv2.imshow ('RPS Game', frame)
            key = cv2.waitKey(125)
            if key == 13: #Press "ENTER" to start running the game.
                start_time = datetime.now()
                diff_time = (datetime.now() - start_time).seconds
                while diff_time >= 0: # While time is greater than 0 do while loop to countdown the time.
                    ret, frame = cap.read()
                    font_1 = cv2.FONT_HERSHEY_TRIPLEX
                    countdown_timer = str(f'STARTING IN: {diff_time}')
                    frame = cv2.putText(frame, str(datetime.now()), (10, 30), font_2, 1, (80, 255, 255), 2, cv2.LINE_AA)
                    frame = cv2.putText(frame, countdown_timer, (200, 220), font_1, 1, (180, 255, 180), 2, cv2.LINE_AA)
                    frame = cv2.putText(frame, stop, (10, 460), font_2, 1, (80, 255, 255), 2, cv2.LINE_AA)
                    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                    cv2.imshow ('RPS Game', frame)
                    diff_time = t - (datetime.now() - start_time).seconds
                    key = cv2.waitKey(125)
                    if key & key == ord('s'): #Press "s" to stop running the loop.
                        break
                    
                else: # Elese, while "computer_wins" and "user_wins" are less than 3 rounds do while loop to get the winner.
                    while computer_wins < 3 and computer_wins >= 0 or user_wins < 3 and user_wins >= 0:
                
                        number_rounds += 1
                        print (f'\nThis is round number: {number_rounds}\n')
                
                        ret, frame = cap.read()
                        frame = cv2.putText(frame, str(datetime.now()), (10, 30), font_2, 1, (80, 255, 255), 2, cv2.LINE_AA)
                        frame = cv2.putText(frame, stop, (10, 460), font_2, 1, (80, 255, 255), 2, cv2.LINE_AA)
                        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                        image_np = np.array(resized_frame)
                        normalized_image = (image_np.astype(np.float32) / 127.0) - 1
                        data[0] = normalized_image
                        prediction = model.predict(data)
                        max_index_prediction = np.argmax(prediction[0])
                        user_choice = self.choice_list[max_index_prediction] # Getting the user choice prediction.
                        cv2.imshow('RPS Game', frame)
                        
                        print (f'{user_choice}\n')
                        computer_choice = self.get_computer_choise(self) # Getting computer choice prediction.
                            
                
                        if computer_choice == "Rock" and user_choice == "Scissors" or computer_choice == "Paper" and user_choice == "Rock" or computer_choice == "Scissors" and user_choice == "Paper":
                            print (f'User choice: {user_choice}')
                            print ('You lost!')
                            computer_wins += 1
                            user_wins -= 1 
                    
                        elif user_choice == "Paper" and computer_choice == "Rock" or user_choice == "Rock" and computer_choice == "Scissors" or user_choice == "Scissors" and computer_choice == "Paper":
                            print (f'User choice: {user_choice}')
                            print ('You won!')
                            computer_wins -= 1
                            user_wins += 1
        
                        elif computer_choice == "Nothing" and user_choice == "Nothing" or computer_choice == "Nothing" or user_choice == "Nothing":
                            print (f'User choice: {user_choice}')
                            print (f'\nNo one has won this round. Please, continue playing.\n')
                            computer_wins = 0
                            user_wins = 0
                    
                        elif computer_choice == user_choice:
                            print (f'User choice: {user_choice}')
                            print (f'\nIt is a round tie! Please, continue playing.\n')
                            computer_wins = 0 
                            user_wins = 0
                            
                        print (f'\n******************************R-P-S******************************')
                        key = cv2.waitKey(1000)
                        if key & key == ord('s'): #Press "s" to stop running the loop.
                            break
                        
                    if computer_wins == 3 and user_wins < 3:
                        print (f'\nComputer has won {computer_wins} times in a row. You lost the game.\n')
                        print (f'******************************R-P-S******************************')
            
                    elif user_wins == 3 and computer_wins < 3:
                        print (f'\nYou have won {user_wins} times in a row. Congratulations, you won the game!\n')
                        print (f'******************************R-P-S******************************')
                        
                    elif computer_wins == 3 and user_wins == 3:
                        print (f'\nNo one has won the game. It is a tie!\n')
                
            elif key & key == ord('q'): # Press "q" to close the window
                break
        cap.release() # After the loop release the cap object
        cv2.destroyAllWindows() # Destroy all the windows
        return self.get_prediction
   
def play():
    '''
    The play function, to get the winner of the game, set to any.
    
    Variable:
    ---------
    play: Any
        Is running the method "self.get_prediction" of the class "RPS".
  
    Returns:
    -------
    play: Any
        Returns the variable of the function.
    '''
    print (f'\n=====================WELCOME TO R-P-S GAME!=====================')
    play = RPS.get_prediction(RPS)
    print(f'\nThank you for playing the R-P-S game!\n')
    print (f'========================SEE YOU NEXT TIME========================\n')
    return play
        
'''
Instantiating the "play" function. 
'''
play_game = play()