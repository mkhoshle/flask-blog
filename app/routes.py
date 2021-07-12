from app import app
from flask import render_template, send_from_directory
from flask import jsonify

from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db
import os


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/blog', methods=['GET'])
def blog():
    return render_template('blog.html', title='Blog')

@app.route('/portfolio', methods=['GET'])
def portfolio():
    return render_template('portfolio.html', title='Portfolio')

@app.route('/cv', methods=['GET'])
def cv():
    return render_template('cv.html', title='My CV')

@app.route('/health', methods=['GET'])
def health():
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

@app.route('/register', methods=['GET','POST'])
def register()):
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f"User {username} is already registered."

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return f"User {username} created successfully"
        else:
            return error, 418

    ## TODO: Return a restister page
    return "Register Page not yet implemented", 501

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            return "Login Successful", 200 
        else:
            return error, 418
    
    ## TODO: Return a login page
    return "Login Page not yet implemented", 501



