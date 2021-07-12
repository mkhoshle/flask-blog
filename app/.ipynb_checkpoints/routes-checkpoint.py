from app import app
from flask import render_template, send_from_directory
from flask import jsonify

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




