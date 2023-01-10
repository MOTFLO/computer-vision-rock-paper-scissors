# Computer Vision RPS
## Milestone 1
#### This milestone is covering the prerequisite content that is necessary for the Computer Vision RPS project, and the first step is to set up the GitHub enviroment, to track any changes to the project, then saving the changes online, in a GitHub repository. 

## Milestone 2
#### To create the Computer Vision RPS project, first is created an image prject model, containing four types of classes: Rock, Paper, Scissor and Nothing. Each class is trained with the corresponding image, using device camera and the Teachable - Machine platform, which can be found at: 
```
https://teachablemachine.withgoogle.com/
```
#### The model that has been trained in this project is used for the Rock-Paper-Scissors game, where each class hass a corresponding image patern, that will match with the player image shown to the camera. 
#### The way how the image project model can be created is as it follows:
* Click on the link that has been provided above
* On the page, click "Get Started"
* On the next page, select on what type of project to teach a machine: Image Project, Audio Project or Pose Project. As example in this project has been selected the Image Project, teaching based on images.
* Next, select the image model, which could be: Standard/Embedded. For this case scenario has been used the Standard Image Model
* On the following page, you can create a class, add image samples(using a webcam/uploading from a device), train the model and after preview, to see how is running the trained model.
* Final step is to download the trained model using one of the following options(Tensorflow.js, Tensorflow or Tensorflow Lite), according to the project requirements. Based on the selected option, the trained model can be exported as a shared link or a converted file and based on the conversion type, downloaded on your local machine. Also, there are provided code snippets to use the model.

## Milestone 3
#### This milestone covers the esential of how to install dependencies in order to make the RPS model to work and it is covering the following: 
* Installing the libraries
* Creating a conda enviroment using the following command: conda create -n <name of enviroment>
* Activating conda enviromentn using the following command: conda activate <name of enviroment>
* Installing the pip: conda install pip
* Installing the libraries: pip install <name of library>
* Deactivating a curent conda enviroment: conda deactivate

## Milestone 4
#### In this milestone is created a Python script which simulates a Rock-Paper-Scissors game, where the code asks the user for an input and then compares the input with the computer's choice, in order to get the winner. The execution of the RPS program has been accomplished as follows:
* Defining "get_computer_choice" and "get_user_choice" method to store user's and computers choices
* Implementing "get_winner" method to get get the winner
* Creating "play" function to simulate the game

### Defining "get_computer_choice" and "get_user_choice" method to store user's and computer's choices
```
import random

print ('\nThis is a Rock-Paper-Scissors game!!\n')

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
```
### Implementing "get_winner" method to get get the winner
```
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
```
### Creating "play" function to simulate the game
```
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

```
## Milestone 5

#### The milestone 5 is covering the final implementation of the Computer Vision RPS project, where the manual "user_choice" function has been replaced by Machine Learning algorithm that has been trained to get the camera input from the user and predict the choice based on the trained model.
#### For the final outcome of the program there has been implmented the "get_prediction" function, to get the winner of the game between computer(computer_choice) and user(user_choice). In oreder to play the game, there have to be used a video camera. 
#### Also, there have been implmented the following functionalities:
* A countdown timer for the game
* The rule of three rounds in order to get a winner
* Implementation of extra functionalities for the game in the frame: countdown time, quit, enter/continue or stop options. 

### A countdown timer for the game
```
/assets/image.png
```
### The rule of three rounds in order to get a winner
```
/assets/image.png
```
### Implementation of extra functionalities for the game in the frame: countdown time, quit, enter/continue or stop options.
```
/assets/image.png
```