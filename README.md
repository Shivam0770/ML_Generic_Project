# ML_Generic_Project

## End To End Generic Machine Learning Project
Creating and Virtual (venv) environment:-
## First create a folder within project. Then direct the command prompt for that folder location and give this command to create new virtual env and install all libraries:-
conda create -p venv python==3.8 -y
## Then after creating this we will use Git commands to create files and push to repository.
## Basic Git Commands:-
git init
Initializes a new Git repository in the current directory.
git clone <repository>
Clones a remote repository to your local machine.
git add <file>
Stages changes in the specified file for the next commit.
git add .
Stages all changes in the current directory.
git commit -m "message"
Commits the staged changes with a descriptive message.
git status
Displays the status of changes in the working directory.
git log
Shows the commit history of the repository.
These are the Git Commands:-
git init
## We will create a readme file inside the project folder and commit that
We will perform these codes:-
git init
git add README.M
git config --global user.name "Shivam Bisht"
git config --global user.email "shivambisht0770@gmail.com"
git commit -m "First Commit"
git branch -m main
git remote add origin https://github.com/Shivam0770/ML_Generic_Project
git remote -v
git push -u origin main
#To pull any file from github we can give git pull and it will get the latest files.:-  git pull
## We will then create a gitignore file in the github so that no file will be removed while committing the change

## Add a file (Setup.py):-
The primary purpose of setup.py is to provide a way to package your Python project into a distributable format.
It defines how to install the package, including specifying dependencies that need to be installed alongside it. This is done using the install_requires parameter.

## -e . 
It helps to directly trigger setup.py file and is used in requirements.txt. It install a Python package in editable mode from the current directory.

## We will create Src folder
In that we will create _init_.py file. So whenever in setup.py the function setup will run for parameter find_package() it will find _init_.py inside src folder and build this whole folder into a package
