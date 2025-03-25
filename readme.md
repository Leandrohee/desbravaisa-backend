# How to start the project

1. Initiate the enviroment and start the server at port 8000

```bash
pipenv shell
python manage.py runserver
```

# Libs used in this project

1. Django
2. python-dotenv

# Django structure

- In django we dont use src or app for a main folder, isntead all the apps are located in the root folder. For an especific folder to be related to a "main role" we use _./core_

This is the structure of the project in django:

├── .gitignore
├── Pipfile
├── config
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
├── core
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
├── manage.py
├── readme.md
├── templates
    └── teste.html
├── teste_html
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── wiki
    ├── django.md
    └── installation.md
