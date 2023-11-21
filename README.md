# Task Manager Web Application

This is a simple web application built with Python Flask, MySQL, HTML and CSS for managing tasks. Users can register, log in, create tasks, and perform various operations related to task management.

## Usage:
    - Register a new account.
    - Log in to your account.
    - Create tasks, update tasks, and delete tasks.
    - Log out of your account.

## Application Structure:
**app/__init__.py:** Initializes the Flask application and sets up the database and login manager.

**config.py**: Contains configuration settings, including the MySQL database URI.

**app/routes.py:** Defines the routes and views for the web application. Handles user registration, login, and task management.

**app/models.py:** Defines the database models for User and Task.

**templates/:** Contains HTML templates for user interfaces.

**static/css/style.css:** Stylesheet for the HTML templates.

## Getting Started

### Prerequisites

- Python 3.x
- MySQL server

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/baldez300/Task-Management-Web-App.git
    ```
2. Navigate to the project directory:

   ```bash
   cd Task-Management-Web-App
   ```
3. Create a virtual environment (optional but recommended):

   ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:

   Linux/macOS:

   ```bash
   source venv/bin/activate
   ```

   Windows:

   ```bash
   venv\Scripts\activate
   ```
5. Install the dependencies:

   ```bash
    pip install -r requirements.txt
    ```
6. Create a MySQL database and user for the application. You can use the following commands:

 ```bash
   mysql -u root -p
   ```

   ```sql
   CREATE DATABASE task_manager;
   USE task_manager;
   DROP USER IF EXISTS 'appuser'@'localhost';
   CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON task_manager.* TO 'appuser'@'localhost';
   FLUSH PRIVILEGES;
   EXIT;
   ```
7. Configure the database connection in config.py file with your MySQL username and password:
    ```python
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://appuser:password@localhost/task_manager'
    ```
7. Set the FLASK_APP environment variable:

   Linux/macOS:

   ```bash
   export FLASK_APP=run.py
   ```

   Windows:

   ```bash
   set FLASK_APP=run.py
   ```

9. Create the database tables by running the following commands in the terminal (make sure you are in the project directory) and MySQL is running on your machine:
    
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
### Create user and task tables
    ```bash
    flask db init
    flask db migrate -m "Create user and task tables"
    flask db upgrade

    # Drop the current database
    flask db drop

    # Recreate the database
    flask db create

    # Apply migrations
    flask db upgrade


    ```
10. Run the application:

   ```bash
    python run.py
    ```
11. Open your web browser and go to http://localhost:5000.

