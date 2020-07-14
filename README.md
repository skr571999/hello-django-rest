# ReactDjangoTodoApp

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
