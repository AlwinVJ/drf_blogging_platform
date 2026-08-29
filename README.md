DRF Blog — The Hallway API

A learning-focused blogging platform built with Django REST Framework (DRF). It is a separate implementation from the original server-rendered Django/MVT version of The Hallway.

The goal is to build the backend independently as a REST API and later create a frontend that reproduces The Hallway's user experience while consuming the API.

Project Goal

Traditional Django / MVT version

Browser
   ↓
Django URL
   ↓
Django View
   ↓
Django ORM
   ↓
Django Template
   ↓
HTML

DRF version

Frontend
   ↓
HTTP Request
   ↓
Django REST Framework
   ↓
Serializer / API View
   ↓
Django ORM
   ↓
PostgreSQL
   ↓
JSON Response
   ↓
Frontend

The objective is to understand the architectural difference between a server-rendered Django application and an API-driven application.

Current Status

Phase: Project foundation completed

Project directory created

Python virtual environment created

Git repository initialized

.gitignore configured

Django installed

Django project initialized

Django REST Framework installed

DRF added to INSTALLED_APPS

requirements.txt created

Django system checks passing

Initial Git commit created

Next

PostgreSQL configuration

Environment variable configuration

Database connection

Application structure

Blog models

Serializers

API endpoints

Authentication

JWT

Permissions

Categories

Comments

Search

Filtering

Pagination

Image/file handling

API testing

Production configuration

AWS deployment

The Hallway-style frontend

Frontend/API integration

Technology Stack

Backend

Python

Django

Django REST Framework

Django ORM

Database

PostgreSQL

PostgreSQL will be used from the beginning rather than developing around SQLite and migrating later.

Authentication

The planned API authentication mechanism is JWT-based authentication.

Frontend

The frontend will be created after the API is stable. It will reproduce the visual experience of The Hallway while consuming the DRF API.

Deployment

The project is being developed with AWS deployment in mind. Production configuration will use environment variables for sensitive and environment-specific settings.

Project Structure

The current structure is intentionally minimal:

DRF-Blog/
│
├── .venv/
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md

config/

The Django project configuration package.

settings.py — project configuration

urls.py — root URL configuration

asgi.py — ASGI entry point

wsgi.py — WSGI entry point

manage.py

Django's command-line utility.

Examples:

python manage.py runserver
python manage.py check
python manage.py makemigrations
python manage.py migrate

.venv/

Local Python virtual environment. It is excluded from Git.

requirements.txt

Contains the Python dependencies required by the project.

Local Development Setup

1. Clone the repository

git clone <repository-url>
cd DRF-Blog

2. Create the virtual environment

Windows:

python -m venv .venv

Activate it:

.venv\Scripts\activate

3. Install dependencies

python -m pip install -r requirements.txt

4. Run Django checks

python manage.py check

5. Start the development server

python manage.py runserver

The development server will normally be available at:

http://127.0.0.1:8000/

Database

PostgreSQL is the intended database for both development and production.

Database credentials must never be committed to Git.

Environment-specific values will eventually include:

SECRET_KEY
DEBUG
DATABASE_NAME
DATABASE_USER
DATABASE_PASSWORD
DATABASE_HOST
DATABASE_PORT

A local .env file may be used during development and must remain excluded from version control.

Planned API Architecture

The final API will be organized around resources rather than HTML pages.

A planned structure is:

/api/
│
├── auth/
│   ├── register/
│   ├── login/
│   └── refresh/
│
├── blogs/
│   ├── /
│   └── <id>/
│
├── categories/
│   ├── /
│   └── <id>/
│
└── comments/
    ├── /
    └── <id>/

The exact URL structure will be finalized during implementation.

The API will support the standard HTTP operations:

GET     Retrieve resources
POST    Create resources
PUT     Replace resources
PATCH   Partially update resources
DELETE  Delete resources

Planned Features

Authentication

User registration

Login

JWT access tokens

JWT refresh tokens

Protected API endpoints

User information

Appropriate logout/token invalidation strategy

Blog

Create posts

Retrieve posts

Retrieve individual posts

Update posts

Delete posts

Draft/published status

Featured posts

Slugs

Author information

Created/updated timestamps

Image handling

Categories

Create categories

List categories

Update categories

Delete categories

Filter posts by category

Comments

Create comments

List comments

Update comments

Delete comments

Comment ownership

Permission restrictions

Discovery

Search

Filtering

Pagination

Featured articles

Recent articles

Authorization

The API will distinguish between:

Anonymous users
Authenticated users
Resource owners
Privileged users

For example:

Anonymous user
    └── Read public posts

Authenticated user
    ├── Create posts
    └── Modify their own posts

Other authenticated user
    └── Cannot modify someone else's post

The exact permission rules will be implemented during development.

API-First Development Strategy

The backend will be developed and tested independently of the final frontend.

Build API
   ↓
Test API
   ↓
Validate authentication
   ↓
Validate permissions
   ↓
Validate CRUD
   ↓
Validate search/filtering/pagination
   ↓
Build frontend
   ↓
Connect frontend to API

The API should be usable through:

DRF Browsable API

Postman

Automated API tests

before the final frontend is integrated.

Frontend Goal

After the DRF backend is complete, a separate frontend will be created to reproduce the visual experience of The Hallway.

The frontend will communicate with the backend through HTTP requests and JSON responses.

Example:

The Hallway Frontend
        ↓
fetch()
        ↓
GET /api/blogs/
        ↓
DRF
        ↓
PostgreSQL
        ↓
JSON
        ↓
The Hallway Frontend

The frontend should not depend on Django template context for blog data. This is intentionally different from the original MVT implementation.

Deployment Goal

The application is intended to be deployment-ready for AWS.

Production preparation will include:

Environment-based configuration

PostgreSQL

Production DEBUG configuration

Secure secret management

Allowed hosts configuration

Static file handling

Media file handling

Production WSGI/ASGI configuration

Gunicorn or an appropriate production application server

HTTPS considerations

Database security

AWS-compatible deployment configuration

AWS services will be selected based on their current availability, limitations, and free-tier eligibility at deployment time.

Development Principles

1. Learn before abstracting

DRF functionality will initially be implemented in a straightforward way so the request/response lifecycle is understood before unnecessary abstractions are introduced.

2. API first

The API should be independently functional before frontend integration.

3. Separate backend and frontend responsibilities

The API provides:

Data
Business rules
Authentication
Authorization
Validation

The frontend provides:

Presentation
User interaction
Client-side state
API consumption

4. PostgreSQL from the beginning

Development and production will use the same database technology.

5. Never commit secrets

Credentials, API keys, database passwords, secret keys, and environment-specific configuration must remain outside Git.

6. Test each feature

Every major feature should be verified through API requests before moving to the next layer.

Git Workflow

Development will be incremental.

Example commit progression:

chore: initialize Django REST Framework project
chore: configure PostgreSQL
feat: create blog models
feat: implement blog serializers
feat: implement blog CRUD API
feat: implement authentication
feat: implement JWT authentication
feat: implement blog permissions
feat: implement categories API
feat: implement comments API
feat: implement search and filtering
feat: implement pagination
test: add API tests
chore: prepare application for production
feat: add Hallway frontend
feat: integrate frontend with DRF API

Feature branches should be used for significant pieces of functionality.

Learning Objective

The primary purpose of this project is not merely to produce another blogging website.

The goal is to understand the practical difference between:

Traditional Django / MVT

Request
  ↓
View
  ↓
Model / ORM
  ↓
Template
  ↓
HTML Response

Django REST Framework

Request
  ↓
API View / ViewSet
  ↓
Serializer
  ↓
Model / ORM
  ↓
JSON Response
  ↓
Frontend

The completed projects should provide a practical comparison between these two approaches using a similar blogging product.

License

This project is currently intended as a personal learning and portfolio project.
