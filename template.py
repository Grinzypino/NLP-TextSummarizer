# Template.py creates the project structure i.e. the directories and files as per the structure mentioned below.

import os
from pathlib import Path
import logging

#logging the runtime info, format is set to include the time and message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

#Below is the structure of the project
project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep", #helps in CI/CD pipelines
    f"src/{project_name}/__init__.py",#constructor file for the package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",#contains all utility functions
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",#all model related parameters
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",# all the experiments and trials

]


for filepath in list_of_files:
    filepath = Path(filepath) #this gives the path according to the OS used (For windows uses \ and for linux uses /) 
    filedir, filename = os.path.split(filepath) #splits the path into directory and filename

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)#creates the directory if it does not exist
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):#checks if the file exists or if its empty by checking the size of the file
        with open(filepath,'w') as f:
            pass #pass does nothing, its just a placeholder (jab if, loop, etc. jese statements me koi code nhi likhna ho to pass likhte hain) 
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
