# Helping Hand
[![Gitter](https://badges.gitter.im/ExpressHermesOSC/Helping-Hand.svg)](https://gitter.im/ExpressHermesOSC/Helping-Hand?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

A social platform built for the organizers charity events to connect with each other to organize bigger events and thus help more people.  

## Frontend
The frontend is fast and interactive. It is built with HTML, CSS, Bootstrap 4 and Vanilla JavaScript.

## Backend
The backend is built with Django framework. It uses SQL based database.

## Demo Screenshots
![Register page](https://github.com/ExpressHermes/Helping-Hand/blob/master/preview/register%20page.png)
![Login page](https://github.com/ExpressHermes/Helping-Hand/blob/master/preview/login%20page.png)
![Event creation page](https://github.com/ExpressHermes/Helping-Hand/blob/master/preview/create%20event.png)
![Events List page](https://github.com/ExpressHermes/Helping-Hand/blob/master/preview/events%20list.png)

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

To create superuser, run following command inside Helping-Hand folder
```
python manage.py createsuperuser
```


For a "OperationalError", run the following command
```
python manage.py makemigrations mainapp
python manage.py migrate
 ```
 
