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
