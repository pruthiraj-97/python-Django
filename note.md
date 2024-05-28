-- setup the uv
pip install uv // All things will did using uv
--setup the vertual enviroment
uv venv
-- adctivate vertual enviroment
--install dejango
uv pip install Django
--Initialize the project
Django-admin startproject djangoproject
--TO RUN ANY FILE
py manage.py runserver // runserver for running the server
urls.py file for setting the urls or API

//BACKEND CONTROL FLOW IN DJANGO

  USER ---> req ---> urls.py ---> views(bussiness logic + DB contact) 
                                user  <----   res <--------

//CREATING apps in Django

py manage.py startapp djangoapp(app name)