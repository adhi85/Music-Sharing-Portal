# Music-Sharing-Portal Using Python Django

•	A basic website that allows users to upload music and share it with each other.

## How to run in local environment
1. Clone this project  
```git clone https://github.com/adhi85/Music-Sharing-Portal.git ```   
``` cd Music-Sharing-Portal ```
2. Start a virtual environment
```
virtualenv venv
venv\scripts\activate
```
3. Install the requirements by   
`` pip install -r requirements.txt``

4. Since this is deployed change the database back to SQLite in settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} 
```
5. Delete the existing migrations (0001_initial.py) in base/migrations 
6. Run  
 ``` 
 python manage.py makemigrations  
 python manage.py migrate
 ```
7. Run the server  
`` python manage.py runserver ``
8. Access the server at  
 http://127.0.0.1:8000/
 
 ## Deployed Link   
 https://web-production-4a08.up.railway.app/
 
