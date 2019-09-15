# PythonExercises

## Project Requirements:
- Ubuntu 18.04 LTS(may work in other operating systems too)
- Python version >=3.6
- Git

## Project Setup:
- Open command prompt
- Make sure python version >=3.6 is installed and git installed
- Make a project folder and cd into it. for example: `mkdir Myproject && cd Myproject`
- git clone the project from here and cd into the cloned folder. for example: `git clone https://github.com/ShaonMahmood/PythonExercises.git && cd PythonExercises`
- Create a python3 virtual environment using command `python3 -m venv env`
- Enter into the virtual environment using `source env/bin/activate`
- install the requirements using `pip install -r requirements.txt`

## Steps to run assignment 1:
Assignment 1 solution is given in two ways. One,in a notebook explaning in depth details and the other in a .py file.Below are the steps to run them:
### Run csv_processing.py file:
- cd into CSV_file_processing directory from root directory. for example: `cd CSV_file_processing`
- this script should be run with a command line argument specifying the csv data url. Run format:
`python csv_processing.py <csv_data_url>`
- run the script with the command `python csv_processing.py "https://press.radiocut.fm/bicycle-travels-jan-2018.csv`
- see the output and enjoy!!

### Run the notebook file:
- cd into CSV_file_processing directory from root directory. for example: `cd CSV_file_processing`
- In the command-prompt type `jupyter-notebook` and a browser will pop up. 
- from the browser select the file named csv_processing_notebook.ipynb and start running the code inside

## Steps to run assignment 2:
A django microservice. The steps are:
- make sure virtual environment is active (instructions given in Project setup) 
- cd into the folder django_microservice
- run into the command prompt `python manage.py makemigrations && python manage.py migrate`
- create a superuser using command `python manage.py createsuperuser`
- Run `python manage.py runserver`. default port is 8000.
- go to admin panel by entering url `http://127.0.0.1:8000/admin` in a browser and log in using superuser credentials.
- add category and games from admin panel.
- to see the list of games go to url: `http://127.0.0.1:8000/api/v1/games`. a query parameter can also be given named category_id. for example `http://127.0.0.1:8000/api/v1/games/?category_id=1`
