import numpy as np
from flask import request, render_template
from application import app
import requests
import random

@app.route('/randomnumber1', methods=["POST"])
def makerandomnum1():
    rand_num1=random.randint(1,100)
   # print(rand_num1)
    return rand_num1
