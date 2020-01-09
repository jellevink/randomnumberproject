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

@app.route('/', methods=["GET","POST"])
def combine():
    random_number1 = requests.get('http://localhost:5001').text
    random_number2 = requests.get('http://localhost:5002').text
    print(random_number1)
    print(random_number2)
    randoms = str(int(random_number1)+int(random_number2))
    print(randoms)
    return randoms
print(combine())

