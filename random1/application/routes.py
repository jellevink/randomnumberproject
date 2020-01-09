import numpy as np
from flask import request, render_template
from application import app
import requests
import random

@app.route('/', methods=["GET"])
def makerandomnum1():
    rand_num1=str(random.randint(1,10))
    print(rand_num1)
    return rand_num1
print(makerandomnum1())
