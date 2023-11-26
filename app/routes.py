# app/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from .models import User, Task

blueprint = Blueprint('app', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('app.index'))

    if request.method == 'POST':
        print(request.form)
        firstname = request.form['first_name']
        lastname = request.form['last_name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        new_user = User(firstname=firstname, lastname=lastname, email=email, username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('app.login'))

    return render_template('register.html')

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('app.index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            return redirect(url_for('app.index'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')

    return render_template('login.html')

@blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    if request.method == 'POST':
        logout_user()
        flash('You have been logged out.', 'success')
        return redirect(url_for('app.login'))
    return render_template('index.html')

@blueprint.route('/')
@login_required
def index():
    return render_template('index.html')

@blueprint.route('/tasks')
@login_required
def get_all_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('get_all_tasks.html', tasks=tasks)

@blueprint.route('/tasks/new', methods=['GET', 'POST'])
@login_required
def create_new_task():
    if request.method == 'POST':
        # Get task details from the form
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']
        status = request.form['status']

        # Create a new task
        create_new_task = Task(
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            status=status,
            user_id=current_user.id
        )

        # Add the task to the database
        db.session.add(create_new_task)
        db.session.commit()

        flash('Task created successfully!', 'success')
        return redirect(url_for('app.get_all_tasks'))

    return render_template('create_new_task.html')

@blueprint.route('/tasks/<int:task_id>')
@login_required
def get_task_by_id(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('get_task_by_id.html', task=task)

@blueprint.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        # Update task details
        task.title = request.form['title']
        task.description = request.form['description']
        task.due_date = request.form['due_date']
        task.priority = request.form['priority']
        task.status = request.form['status']

        # Commit changes to the database
        db.session.commit()

        flash('Task updated successfully!', 'success')
        return redirect(url_for('app.task', task_id=task.id))

    return render_template('edit_task.html', task=task)

@blueprint.route('/tasks/<int:task_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        # Remove the task from the database
        db.session.delete(task)
        db.session.commit()

        flash('Task deleted successfully!', 'success')
        return redirect(url_for('app.get_all_tasks'))

    return render_template('delete_task.html', task=task)
