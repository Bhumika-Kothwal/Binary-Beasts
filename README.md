# Driver-Drowsiness Detection

### Team name: Binary Beasts

## Team members
* Bhumika Kothwal - kothwalbhumika@gmail.com
* Donovan Crasta - donovancrasta11954@gmail.com
* Nishtha Sainger - nish279rs@gmail.com
* Pratam Jain - pratamjain1234@gmail.com

## Mentors
* Priyesh Vakharia
* Parth Shah
* Saif Kazi

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Description](#description)
* [Technology Stack](#technology-stack)
* [Project Setup](#project-setup)
* [Usage](#usage)
* [File Structure](#file-structure)
* [Applications](#applications)
* [Future Scope](#future-scope)
* [Screenshots](#screenshots)
    
        
## Description
This Project is a combination of computer vision , front-end and back-end development . In this with the help of a web camera a continous image (known as video) 
is taken as input and with the of some  eucledian mathematics , algorithims , inbuilt packages and models of python , if the user is found to be sleepy/drowsy an alarm beeps making the user aware of conditions so that proper care can be taken of his/her sleepy situation. 

It has an accuracy of approximately 95% and a reaction time of less than 1 second making it more efficient for using it.    

It can also be used by students to keep themselves awake while studing as the alarm will wake them up whenever they feel drowsy allowing them to continue their studies without any tension of drowsing off.
    
        
* GitHub repo link: [Binary-Beasts](https://github.com/Bhumika-Kothwal/Binary-Beasts)
* Drive link: [Drive link here](https://drive.google.com/)
    
        
## Technology stack

Tools and technologies that you learnt and used in the project.

1. Python
2. Machine Learning
3. OpenCV
4. Javascript
5. HTML
6. CSS (basic)
    
        
## Project Setup
> See [SETUP.md](https://github.com/Bhumika-Kothwal/Binary-Beasts/blob/master/SETUP.md) for the installation steps.
    
        
## Usage
* Clone the repo
```sh
$ git clone https://github.com/Bhumika-Kothwal/Binary-Beasts.git
``` 
* Run the webapp.py file using the command -
```sh
$ python webapp.py
```
* Go to the link which shows on terminal.   
    
Click [here]() to understand how to go about with the web-app.  
    
        
## File Structure   
```sh
    .  
    ├── fonts 
    ├── img 
    ├── mail 
    ├── alarm.wav                           # alarm file
    ├── shape_predictor_68_face_landmarks   # dlib classifier to detect facial landmarks
    ├── static                   
    │   ├── js                              # contains .js files    
    │   ├── styles                          # contains .css files       
    │   └── demo.mp4                        # contains demo of our project          
    ├── templates                           # conatins HTML pages  
    │   ├── demo.html                       # contains demo video
    │   ├── start.html                      # live drowsiness detection page
    │   └── index.html                      # home page
    ├── drowsiness_detection                # conatins python code    
    │   ├── eye_yawn_detection              # python code for drowsiness detection
    │   └── __init_.py       
    ├── webapp.py                           # conatins server-side Flask code   
    ├── SETUP.md                            # contains installation instructions of different modules
    └── README.md                          
``` 
    
        
## Applications
> It can be used to detect if a driver is drowsy or not during driving and plays alarm if the driver is drowsy resulting in preventing any accidents in near future.  
  
> It can also be used by students to keep themselves awake while studing as the alarm will wake them up whenever they feel drowsy allowing them to continue their studies without any tension of drowsing off.
    
        
## Future scope
> The project now uses the web-cam to capture the images of driver to process upon. Further work includes -
- [ ] Providing feature to capture images using Raspberry-Pi or other external camera
- [ ] Building this model into a hardware which can be directly fixed onto a place  
- [ ] Making this into a web-application and can be used by any external server as well

    
        
## Screenshots
Add a few screenshots here to give the viewer a quick idea of what your project looks like. After all, a picture speaks a thousand words.

![Screenshot alt text](https://edtimes.in/wp-content/uploads/2018/09/NikeMeme10-640x633.jpg "Here is a screenshot")
        
