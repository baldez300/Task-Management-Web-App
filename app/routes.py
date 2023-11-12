# app/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from .models import User

blueprint = Blueprint('app', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('app.index'))  # Assuming you have an 'index' route in your blueprint

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('app.login'))  # Assuming you have a 'login' route in your blueprint

    return render_template('register.html')

# Add the remaining routes here...
@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('app.index'))  # Replace 'app.index' with your actual index route

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            return redirect(url_for('app.index'))  # Replace 'app.index' with your actual index route
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
def tasks():
    return render_template('tasks.html')


@blueprint.route('/tasks/new')
@login_required
def new_task():
    return render_template('new_task.html')


@blueprint.route('/tasks/<int:task_id>')
@login_required
def task(task_id):
    return render_template('task.html')


@blueprint.route('/tasks/<int:task_id>/edit')
@login_required
def edit_task(task_id):
    return render_template('edit_task.html')


@blueprint.route('/tasks/<int:task_id>/delete')
@login_required
def delete_task(task_id):
    return render_template('delete_task.html')

