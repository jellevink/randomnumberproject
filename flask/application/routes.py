from flask import render_template, request, session
from application import app
import requests
import os

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    combined=requests.get('http://localhost:5003').text
    print(combined)

    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('home.html', title='About')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

