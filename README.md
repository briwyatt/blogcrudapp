# Django CRUD Example Apps

This is a small Django project to demonstrate Django CRUD functionality, it
consist of 1 small application:

- blog: Implement CRUD for blog posts.


## Install Required Packages

The Django CRUD project only need a single Python package "Django", it was built and
tested with Django 1.11 version. 

## Running the Application

Before running the application we need to create the needed DB tables:

    ./manage.py migrate

Now you can run the development web server:

    ./manage.py runserver

To access the applications go to the URL <http://localhost:8000/>
