# Chatbots_BE
 
* Chatbots is a open source project for the time being and maybe used for the profitable use in the future. As of its development phase nothing is guaranteed.

* Initially idea of this project is still very vague and maybe changed in the future. However, as of now idea is to make a website containing a vast set of chatbots for different type of usages. 

## This is frontend code of Chatbots
* This project has been divided into frontend and backend.
* This is the backend of the project.
* To set it up in your system you need to follow below steps:
1. First, clone this repository in your local system.
2. You will need python in your system so make sure it is already there in your system.
3. Once you have it you will have to open this repository in your VS code or any other IDE of your liking. ( VS code is recommended for its capabilities over all others).
4. Once you are done with previous step you will need to create an environment for these project in root directory using below steps depending your operating system:
    - For Windows:
        - To create a virtual environment : python -m venv venv
        - To activate virtual environment : .\venv\Scripts\activate
    - For Linux / macOS:
        - To create a virtual environment : python3 -m venv venv
        - To activate virtual environment : source venv/bin/activate
        - if python3 does not work in your system try python or check your python installation.
5. Once your environment is active, in your local system just make sure you are in main directory (i.e. ....Chatbots_BE/Chatbots_BE) otherwise use cd to be in the main directory.
6. Once you are in main directory hit pip install -r requirements.txt, it will install required dependencies in your system.
7. Now for next steps you will need backend setup in your system so make sure you have already done that in your system.
8. Once your frontend setup is also done just hit python manage.py runserver to run your backend and you are all set from backend side.
9. Moreover, if you don't want to use default configuration of database you may need to alter logic of database in settings.py.

### New ideas for this project is always welcomed.