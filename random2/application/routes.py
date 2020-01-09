import numpy as np
from flask import request, render_template
#from application import app
import requests
import random

@app.route('/randomnumber2', methods=["POST"])
def makerandomnum2():
    rand_num2=random.randint(1,100)
   # print(rand_num2)
    return rand_num2
