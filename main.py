from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Nothing worth seeing here"

@app.route('/login')
def login():
    return render_template("login_page.html")