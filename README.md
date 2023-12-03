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

12. If you want to clean up the migration history completely, you can manually delete the migrations directory and the alembic_version table in your database. 

``` bash
rm -r migrations
```

``` sql
USE task_manager;
DROP TABLE alembic_version;
DROP TABLE task;
DROP TABLE user;

```

Then, run the following commands to create a new migration history and upgrade the database:

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
12. After you have finished using the application, you can deactivate the virtual environment:

    ```bash
    deactivate
    ```
13. If you want to delete the virtual environment, you can simply delete the venv directory. On Linux or macOS, use the following command:

    ```bash
    rm -rf venv
    ```
    On Windows, use the following command:

    ```bash
    rmdir /s venv
    ```
14. After dropping the database, you can create a new database and user for the application by following those steps:

This command initializes the migration environment. It creates a migrations directory in the project root directory.

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
15. If you want to clean up the migration history completely, you can manually delete the migrations directory and the alembic_version table in your database.

    ```bash
    rm -r migrations
    ```
    ```sql
    USE task_manager;
    DROP TABLE alembic_version;
    DROP TABLE task;
    DROP TABLE user;
    ```
    Then, run the following commands to create a new migration history and upgrade the database:

    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
16. How to make your MariaDB server running from the terminal command line on macOS:

    ```bash
    sudo mysql.server start
    mysql
    ```
    ```sql
    USE task_manager;
    SELECT * FROM user;
    SELECT * FROM task;
    ```
17. How to make your MariaDB server running from the terminal command line on Windows:

    ```bash
    mysqld
    mysql -u root -p
    ```
    ```sql
    USE task_manager;
    SELECT * FROM user;
    SELECT * FROM task;
    ```
18. Then you should be able to see the following tables:

    ```sql
    +------------------------+
    | Tables_in_task_manager |
    +------------------------+
    | alembic_version        |
    | task                   |
    | user                   |
    +------------------------+
    3 rows in set (0.00 sec)
    ```
19. An example picture of the user and task tables:

    ![alt text](app/templates/image/db_picture.png)
