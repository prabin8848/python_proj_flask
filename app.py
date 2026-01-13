from flask import Flask,render_template

app = Flask(__name__)

subjects = ['python','Database','Data Science','java']

@app.route("/")
def index():
    return render_template('index.html',name='Prabin')

@app.route("/about")
def about():
    return 'I am Prabin.Welcome to my class'

@app.route("/contact")
def contact():
    return "Email: prabinraytharu811@gmail.com"