# Music-Sharing-Portal Using Python Django
## About
• A basic website that allows users to upload music and share it with each other.   
• Users can register and login on the platform using Email.   
• Users can upload music files on the platform and have different visibility options i.e as public/private/protected.    
• Public Music File: Visible to all the users.    
• Private Music File: Visible to the user who has uploaded it.    
• Protected Music File: Visible to users who have access to the file using email.   
(When User uploads the music file user can add email addresses of other Users that can acces it.). 

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
 
 PS: Only focused on Logic and not frontend UI.
 
 
 
