from main import app
from flask import jsonify, render_template, request

@app.route('/')
@app.route('/index')
def index():
    return jsonify({'message':'Nothing worth seeing here'})

# @app.route('/login')
# def login():
#     return render_template("login_page.html")

# @app.route('/authenticate', methods=['POST'])
# def authenticate():

#     return request.form['password']