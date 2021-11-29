# Helping Hand
[![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://join.slack.com/t/slack-coh8135/shared_invite/zt-zrefahmo-NcRHial9jkoZrzZEcFMMTA)

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

- First you need to clone the repository
  ```
  git clone https://github.com/ExpressHermes/Helping-Hand.git
  ```

- Install all required dependencies in a virtual environment
  ```
  cd <directory_name>
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

- Run the backend on local server
  ```
  cd <directory_name>
  source venv/bin/activate
  cd Helping-Hand
  python manage.py runserver
  ```

- To create superuser, run following command inside Helping-Hand folder
  ```
  python manage.py createsuperuser
  ```


- For a "OperationalError", run the following command
  ```
  python manage.py makemigrations mainapp
  python manage.py migrate
  ```

## Contribution
- Fork and clone the repo.  
- To avoid merge conflicts, make sure to set upstream in your git.
    ```
    git remote add upstream https://github.com/ExpressHermes/Helping-Hand.git
    ```
- Whenever you want to pull changes from main repo, run:
    ```
    git pull upstream master
    ```
- Create your feature branch
    ```
    git checkout -b <feature-name>
    ```
- Commit your changes
    ```
    git commit -am "Meaningful commit message"
    ```
- Push to the branch
    ```
    git push origin <feature-name>
    ```

- If you see any bug or you have a feature suggestion, create an issue.
- Start working on an issue only after it has been approved by the maintainer.
- Wait till the end of the day to get the reply on an issue or review of a PR.
