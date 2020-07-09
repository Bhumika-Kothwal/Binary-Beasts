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

## Description
Add your project description here. Your project description should cover how your website/app works. That way you can convey what your project is without the need for anyone to view the code. A more detailed readme in your project repository is encouraged, which can include build and use instructions etc.

* Use bullet points for any feature descriptions you may want to add

```bash
    Add appropriate code snippets here (4 spaces indent)
```

Don't forget to replace the link here with **_your own Github repository_** link.

Along with this, add the link of the drive folder that contains the app APK/Screenshots/Screen Recordings. If you have hosted your project on the web, add that link as well.

* GitHub repo link: [Link to repository](https://github.com/your-repo-link)
* Drive link: [Drive link here](https://drive.google.com/)
* Website link: [Website link here](www.google.com)

## Technology stack

Tools and technologies that you learnt and used in the project.

1. Python
2. Machine Learning
3. Flask-SocketIO
4. Javascript
5. HTML
6. CSS (basic)

## Project Setup
> See [SETUP.md](https://github.com/Bhumika-Kothwal/Binary-Beasts/blob/master/SETUP.md) for the installation steps.

## Usage
Clone the repo
```sh
git clone https://github.com/Bhumika-Kothwal/Binary-Beasts.git
``` 
  
The file structure is as follows -   
```sh
    Drowsiness detection app  
    ├── static                   
    │   ├── js                            # contains .js files    
    │   ├── models                        # contains face detection and face landmark detection models      
    │   └── styles                        # contains CSS files for HTML page styling          
    ├── templates                         # conatins HTML pages     
    │   └── index.html                    # app page
    ├── python_code                       # conatins python code    
    │   ├── drowsiness_detection.py       # python code for drowsiness detection
    │   └── __init_.py        
    └── app.py                            # conatins server-side Flask-SocketIO code   
``` 


## Applications
> It can be used to detect if a driver is drowsy or not during driving and plays alarm if the driver is drowsy resulting in preventing any accidents in near future.  
  
> It can also be used by students to keep themselves awake while studing as the alarm will wake them up whenever they feel drowsy allowing them to continue their studies without any tension of drowsing off.

## Future scope
> The project now uses the web-cam to capture the images of driver to process upon. Further work includes -
- [ ] Providing feature to capture images using Raspberry-Pi or other external camera
- [ ] Building this model into a hardware which can be directly fixed onto a place

## Screenshots
Add a few screenshots here to give the viewer a quick idea of what your project looks like. After all, a picture speaks a thousand words.

![Screenshot alt text](https://edtimes.in/wp-content/uploads/2018/09/NikeMeme10-640x633.jpg "Here is a screenshot")
