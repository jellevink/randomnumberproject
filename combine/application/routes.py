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
            prize = 10000
        if random_number2 == 2:
            prize = 20000
        if random_number2 == 3:
            prize = 30000
        if random_number2 == 4:
            prize = 40000
        if random_number2 == 5:
            prize = 50000
        if random_number2 == 6:
            prize = 60000
        if random_number2 == 7:
            prize = 70000
        if random_number2 == 8:
            prize = 80000
        if random_number2 == 9:
            prize = 90000
        if random_number2 == 10:
            prize = 100000
    else:
        prize = "tee"
    print(prize)
    return str(prize)

print(combine())

