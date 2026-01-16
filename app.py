from flask import Flask,render_template,abort
from db_connect import get_connection
app = Flask(__name__)

subjects = ['python','Database','Data Science','java']

@app.route("/")
def index():
    return render_template('index.html',name='Prabin',subjects=subjects)

@app.route("/about")
def about():
    return 'I am Prabin.Welcome to my class'

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/students")
def students():
    with get_connection().cursor() as cur:
        cur.execute("SELECT * FROM student")
        students = cur.fetchall()
        return render_template("student.html",students=students)
    
if __name__=='__main__':
    app.run(debug=True)