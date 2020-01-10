from flask import render_template, request, session
from application import app
from application.models import User
import requests
import os

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    response=requests.get('http://localhost:5003').text
    print(response)

    return render_template('home.html', title='Home', data=response)

@app.route('/about')
def about():
    return render_template('home.html', title='About')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/users')
def users():
    postData = User.query.all()
    print(post.first_name)
    return render_template('users.html', title='Users', users=postData)
