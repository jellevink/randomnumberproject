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
    dummyvariable = 1
    print(random_number1)
    print(random_number2)
    #randoms = str(int(random_number1)+int(random_number2))
    #print(randoms)
    if random_number1 == 1:
        mid = "push-ups"
    if random_number1 == 2:
        mid = "crunches"
    if random_number1 == 3:
        mid = "sit-ups"
    if random_number1 == 4:
        mid = "leg raises"
    if random_number1 == 5:
        mid = "pull-ups"
    if random_number1 == 6:
        mid = "squats"
    if random_number1 == 7:
        mid = "lunges"
    if random_number1 == 8:
        mid = "burpees"
    if random_number1 == 9:
        mid = "glute bridges"
    if random_number1 == 10:
        mid = "spider crawls"
    if dummyvariable == 1:
        if random_number2 == 1:
            mid2 = 4
        if random_number2 == 2:
            mid2 = 5
        if random_number2 == 3:
            mid2 = 6
        if random_number2 == 4:
            mid2 = 8
        if random_number2 == 5:
            mid2 = 10
        if random_number2 == 6:
            mid2 = 12
        if random_number2 == 7:
            mid2 = 15
        if random_number2 == 8:
            mid2 = 20
        if random_number2 == 9:
            mid2 = 25
        if random_number2 == 10:
            mid2 = 30
    if dummyvariable == 2: 
        if random_number2 == 1:
            mid2 = 40
        if random_number2 == 2:
            mid2 = 50
        if random_number2 == 3:
            mid2 = 60
        if random_number2 == 4:
            mid2 = 80
        if random_number2 == 5:
            mid2 = 100
        if random_number2 == 6:
            mid2 = 120
        if random_number2 == 7:
            mid2 = 150
        if random_number2 == 8:
            mid2 = 200
        if random_number2 == 9:
            mid2 = 250
        if random_number2 == 10:
            mid2 = 300
    prize = "Today, you should do " + str(mid2) + " " + mid + "!!!"
    print(prize)
    return str(prize)

print(combine())
