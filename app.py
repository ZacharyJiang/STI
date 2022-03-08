# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:08:06 2022

@author: Zijie Jiang
"""

import joblib
from flask import Flask
app = Flask(__name__)

from flask import request,render_template

# decorator, must run the function before running any subsequent one
@app.route("/", methods = ["GET","POST"]) 

def index():
    if request.method == "POST":
        Nikkei = request.form.get("Nikkei")
        print(Nikkei)
        model1 = joblib.load("STI_REG")
        pred1 = model1.predict([[Nikkei]]) 
        str1 = "The prediction for STI using Regression is: "+str(pred1)
        return(render_template("index.html",result1=str1))
    else:
        return(render_template("index.html",result1="2"))
               
if __name__ == "__main__":
    app.run("127.0.0.1",port="1111")

