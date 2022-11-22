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
