from flask import request
from application import app
import requests
import os
import random
import string


@app.route('/', methods=["GET","POST"])
def combine():
    random_number1 = int(requests.get('http://random1:5001').text)
    random_number2 = int(requests.get('http://random2:5002').text)
    print(random_number1)
    print(random_number2)
    #randoms = str(int(random_number1)+int(random_number2))
    #print(randoms)
    if random_number1 % 3 == 0:
        if random_number2 == 1:
            prize = 100
        if random_number2 == 2:
            prize = 200
        if random_number2 == 3:
            prize = 300
        if random_number2 == 4:
            prize = 400
        if random_number2 == 5:
            prize = 500
        if random_number2 == 6:
            prize = 600
        if random_number2 == 7:
            prize = 700
        if random_number2 == 8:
            prize = 800
        if random_number2 == 9:
            prize = 900
        if random_number2 == 10:
            prize = 1000
    else:
        prize = 0
    print(prize)
    return str(prize)

print(combine())

