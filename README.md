Coffee Shop
===========

Welcome to the Task Manager project! This Django application is designed to manage tasks efficiently.

Requirements
------------

*   **Python 3.12**

Installation Guide
------------------

Follow these steps to get the project up and running on your local machine.

### 1\. Clone the Repository

Clone the project repository from GitHub to your local machine.

```bash
git git@github.com:JhonSoto99/task-manager.git
cd task-manager
```

### 2\. Set Up Virtual Environment

Create and activate a virtual environment.


```bash
python3.12 -m venv venv 
source venv/bin/activate 
```

### 3\. Install Dependencies

Install the required Python packages using `pip`.

`pip install -r requirements.txt`

### 4\. Configure Environment Variables

Create a `.env` file in the root of the project. You can use `.env.example` as a template.


`cp .env.example .env`

Update the `.env` file with your database credentials and other necessary configurations.

### 5\. Set Up the Database

This application connects to a PostgreSQL database hosted on AWS RDS. Make sure to configure the database connection in the settings.py file with the appropriate credentials and endpoint.

### 6\. Asynchronous Notifications with Celery

This project uses Celery to handle asynchronous notifications. To ensure notifications are processed correctly, make sure to start the Celery worker with the following command:

`celery -A task_manager worker --loglevel=info`

### 7\. Access the Application

A superuser account already exists with the following credentials:

Username: `admin`
Password: `admin`
Additionally, users can register directly through the web application.


### 8\. Run tests
`python manage.py test`


### 9\. Run the Development Server

Start the Django development server.

```
./manage.py runserver
```

- Access the project by navigating to http://127.0.0.1:8000 in your web browser.
- Access the Api Root by navigating to http://localhost:8000/api/tasks/ in your web browser.

## View the API Documentation:
- Swagger UI: http://127.0.0.1:8000/api/docs/
- Redoc: http://127.0.0.1:8000/api/redoc/

Project Structure
-----------------

*   **tasks**: Handles everything related to tasks.
*   **users**: Manages user authentication.