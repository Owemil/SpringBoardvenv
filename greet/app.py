from flask import Flask

app = Flask=(__name__)


@app.route('/welcome')
def welcome():
    return 'Welcome!'

@app.route('/welcome/home')
def home_msg():
    return "Welcom Home!"

@app.route('/welcome/back')
def back_msg():
    return "Welcome Back!"