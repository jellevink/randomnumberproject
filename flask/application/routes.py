from flask import render_template, request, session, url_for, redirect
from application import app, db, bcrypt
from application.models import User
from application.forms import LoginForm, RegistrationForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required
import requests
import os

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    response=requests.get('http://combine:5003').text
    print(response)

    return render_template('home.html', title='Home', data=response)

@app.route('/register', methods=['GET','POST'])
def register():
    #If user logged in; redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    #Sets up registration form
    form = RegistrationForm()
    if form.validate_on_submit():
        #hash password
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = User(email=form.email.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    password=hashed_pw)
        #adds user to database
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/about')
@login_required
def about():
    return render_template('home.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    #If already logged in, redirect to home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    #Creates the form to log in-in forms.py
    form = LoginForm()
    #If form is valid
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        #If password relates to email
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    #Once logged out, send user to login page
    return redirect(url_for('login'))

@app.route('/account', methods=['GET','POST'])
#User must be logged in to access it
@login_required
def account():
        form = UpdateAccountForm()
        if form.validate_on_submit():
                current_user.first_name = form.first_name.data
                current_user.last_name = form.last_name.data
                current_user.email = form.email.data
                db.session.commit()
        elif request.method == 'GET':
                form.first_name.data = current_user.first_name
                form.last_name.data = current_user.last_name
                form.email.data = current_user.email
        return render_template('account.html', title='Account', form=form)


@app.route('/users')
def users():
    postData = User.query.all()
    print(post.first_name)
    return render_template('users.html', title='Users', users=postData)
