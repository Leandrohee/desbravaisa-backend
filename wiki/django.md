# Usefull comands

```bash
django-admin help                           #Help commands
django-admin startproject config .          #Initiate the project
python manage.py runserver                  #Start the server
```

# Using enviroment variables

```python
from dotenv import load_doten

load_dotenv()

VARIABLE = os.getenv('VARIABLE')
VARIABLE = str(os.getenv('VARIABLE'))       #If need to transform into a string
```

# Templates in Django

If we need to inject direct from the backend, one of the alternatives is to use templates and render

1. Create a folder named template
2. Create an file insed the template folder with your html code
3. Config the settings.py inside config to point the templates to match the created folder

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],               #This is the config needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

4. Import this file in the app/view.py that you require
5. To deal with static file such as css and images in the django itself we need to do others configurations.
   For the purpose of this project i will not use static files right now, but should i need i need to change
   some configs in the config/settings.py and some commands like 'collectstatic'.

# Apps in Django

Django use apps in his arquitecture. Each app is responsable for a part of the project.
Each app has his own structure MVT (model, view, template).

Creating an new app

```bash
django-admin startapp <nameOfTheApp>
```

When creating an app it will create also the MVT structure related to this app.

_After creating the app we need to import into config/settings/INSTALLED_APPS_

# MVT in Django

Django uses MVT in his structure. MVT stands for Model, View, Template and is similtar to MVC

1. Model
2. View
3. Template

# Rest Api

We need to install the djangorestframework in order to build Rest API in django.

Installing

```bash
pipenv install djangorestframework
```

After installing we need to import into INSTALLED_APPS in config/settings

# Database + PostgreSql

We have to install this lib to connect the postgre database into Django

```bash
pipenv install psycopg2
```

How to make sure if the db is connected:

```bash
python manage.py dbshell
exit
```

### How to create an shcema with migrations instead of the sheel

i going to create an schema with migrations instead of creating with the django db shell.

```bash
python manage.py makemigrations --empty <nameOfTheApp> --name <nameOfMigrationFile>
python manage.py makemigrations --empty teste_rest --name create_schema_pessoas
```

this will generate an file inside the folder app/migrations

```python
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunSQL("CREATE SCHEMA IF NOT EXISTS pessoas;")
    ]
```

Creating a table realated to this schema

1. Create the class that is going to be the table
2. Make the migration

```bash
python manage.py makemigrations --name create_table_pessoas
```
