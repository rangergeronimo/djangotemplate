# Create a Simple Django Boilerplate

## Installation

1. Install [Python](https://www.python.org/downloads/).
2. Set up [venv](https://docs.python.org/3/library/venv.html)
3. Activate your virtual environment

```sh
python3 -m venv myvenv
source ./myvenv/bin/activate
```

4. Install [pip](https://pip.pypa.io/en/stable/installing/)

5. Install Django

```sh
pip install django
```
6. Start a  new django project
```sh
django-admin startproject --template https://github.com/rangergeronimo/djangotemplate/archive/master.zip  <project_name>
```
7. Make migrations 
```sh
 python manage.py migrate
```
8. Create super user 
```sh
 python manage.py createsuperuser
```
9. Run sever
```sh
 python manage.py runserver
```
if everything went good, you should a django project running, ready to develop.
Visit http://localhost:8000/ from your browser.
To access the admin page visit http://localhost:8000/admin


