# React Django Todo App

## Intial Installation

```cmd
md ReactDjangoTodoApp
cd ReactDjangoTodoApp
code .

# FrontEnd
npx create-react-app client --use-npm
cd client
npm i react-router-dom
npm start

# Backend
md server
cd server
python -m venv venv
venvS
pip install django
pip install djangorestframework
pip freeze > requirements.txt
django-admin startproject server
rename server src
cd src
python manage.py startapp todo
python manage.py runserver
start opera "http://127.0.0.1:8000/"
```

## Technologies and Tools

- TextEditor - Visual Studio Code
- VSCode Extensions
  - Prettier - for code formatting
  - Python
- Development OS - Window 10
- Frontend - React
- Backend - Django(Django Rest Framework)

## Usage

```cmd
git clone https://github.com/skr571999/ReactDjangoTodoApp.git

cd client
npm install
npm start

cd server
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
cd src
python manage.py runserver
```

<!-- ## Preview Screens -->
