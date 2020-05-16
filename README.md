# Helping Hand
A social platform built for the organizers charity events to connect with each other to organize bigger events and thus help more people.  

## FrontEND
The frontend is fast and interactive. It is built with HTML, CSS, Bootstrap 4 and Vanilla JavaScript.

## Demo Screenshots
    ![Register page](https://github.com/ExpressHermes/Helping-Hand/blob/master/preview/register%20page.png?raw=True)
    ![Login page](https://github.com/ExpressHermes/Helping-Hand/blob/master/preview/login%20page.png?raw=True)
    ![Event creation page](https://github.com/ExpressHermes/Helping-Hand/blob/master/preview/create%20event.png?raw=True)
    ![Events List page](https://github.com/ExpressHermes/Helping-Hand/blob/master/preview/events%20list.png?raw=True)
    
## Backend
The backend is built with Django framework. It uses SQL based database.

## Installation
Make sure following softwares are installed in your computer:
* Python 3
* Git

First you need to clone the repository
```
git clone https://github.com/ExpressHermes/Helping-Hand.git
```

Install all required dependencies in a virtual environment
```
cd <directory_name>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the backend on local server
```
cd <directory_name>
source venv/bin/activate
cd Helping-Hand
python manage.py runserver
```

To create superuser, run following command inside Helpin-Hand folder
```
python manage.py createsuperuser
```


For a "OperationalError", run the following command
```
python manage.py makemigrations mainapp
python manage.py migrate
 ```
 
