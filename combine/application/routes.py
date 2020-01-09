from flask import request
from application import app
import requests
import os
import random
import string

"""@app.route("/makerandomsequence", methods=["POST"])
def makesequence():
    sequence = ""
    sequence = requests.post( "http://flask-number1:5000/randomnumber1")
    randnumber2 = requests.post( "http://flask-number2:5000/randomnumber2")
    return {"sequence":sequence}"""

@app.route('/', methods=["POST"])
def combine():
    random_number1 = requests.post('http://random1:5001')
    random_number2 = requests.post('http://random2:5002')
    return random_number1, "+", random_number2


