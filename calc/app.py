from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def calc_add():
    a = request.args["a"]
    b = request.args["b"]
    
    return add(a,b)

@app.route("/sub")
def calc_sub():
    a = request.args["a"]
    b = request.args["b"]
    
    return sub(a,b)

@app.route("/mult")
def calc_mult():
    a = request.args["a"]
    b = request.args["b"]
    
    return mult(a,b)

@app.route("/div")
def calc_div():
    a = request.args["a"]
    b = request.args["b"]
    
    return div(a,b)

