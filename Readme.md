# Django Blog Application

A simple blog application built with Django that allows users to create, read, update and delete blog posts.

## Features

* View all blog posts on the homepage
* View individual blog post details
* Create and manage posts through the Django Admin panel
* User authentication support
* Responsive styling using CSS
* Automated tests for models, views and URLs

## Technologies Used

* Python
* Django 5.x
* SQLite Database
* HTML
* CSS

## Project Setup

1. Create and activate a virtual environment:

```bash 
# Windows
python -m venv .venv
.venv\Scripts\Activate
#Linux
python3 -m venv .venv
source .venv/bin/activate 
```

2. Install dependencies:

```bash
pip install django
pip install black
```

3. Run database migrations:

```bash
python manage.py migrate
```

4. Create a superuser:

```bash
python manage.py createsuperuser
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Project Structure

```
blog/
├── blog/
├── django_project/
├── templates/
├── static/
│   └── css/
├── manage.py
└── README.md
```

## Running Tests

Run all tests using:

```bash
python manage.py test
```

## Author

Developed as a Django learning project demonstrating CRUD functionality, database models, views, templates, static files and testing.
