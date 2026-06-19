# Django Blog Application

A simple and user-friendly blog application built with Django. The application allows users to create accounts, log in and manage blog posts through a clean web interface.

## Features

* User Registration (Sign Up)
* User Authentication (Login & Logout)
* Create Blog Posts
* View All Blog Posts
* View Individual Blog Post Details
* Edit Existing Posts
* Delete Posts
* Django Admin Panel
* SQLite Database
* Responsive and Modern User Interface

## Technologies Used

* Python
* Django
* HTML5
* CSS3
* SQLite

## Project Structure

```text
django_blog/
│
├── blog/
│
├── accounts/
│
├── static/
│
├── templates/
│
├── manage.py
└── db.sqlite3
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd django_blog
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install django
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Admin Panel

Access the Django admin panel at:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser credentials created earlier to log in.

## Usage

1. Create an account using the Sign Up page.
2. Log in to the application.
3. Create new blog posts.
4. View and manage existing posts.
5. Edit or delete posts when necessary.
6. Log out securely.

## Author

Developed as a Django Blog CRUD Application project.

