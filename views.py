from main import app
from flask import jsonify, render_template, request

@app.route('/')
@app.route('/index')
def index():
    return render_template('login_page.html')

@app.route('/signup')
def signup():
    return render_template('signup_page.html')


@app.route('/dashboard')
def dashboard():
    return "<h1>Hello, I'm dashboard page</h1>"

# @app.route('/login')
# def login():
#     return render_template("login_page.html")

# @app.route('/authenticate', methods=['POST'])
# def authenticate():

#     return request.form['password']