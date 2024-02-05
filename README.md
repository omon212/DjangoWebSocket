## 1) Creating a virtual environment for macOS
```angular2html
python3 -m venv env
```
## 2) Activate virtual environment for macOS
```angular2html
source env/bin/activate
```
## 2) Install requirements.txt
```angular2html 
pip install -r requirements.txt
```
## 3) Migrate and Makemigrations
```angular2html
python manage.py makemigrations
python manage.py migrate
```
## 4) Run Project
```angular2html
uvicorn Core.asgi:application   
```