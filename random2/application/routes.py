import numpy as np
from flask import request, render_template
from application import app
import requests
import random

@app.route('/', methods=["GET"])
def makerandomnum2():
    rand_num2=str(random.randint(1,100))
    print(rand_num2)
    return rand_num2
print(makerandomnum2())
