# import os
# from flask import render_template, send_from_directory
# from flask import jsonify

from flask import Flask, request, render_template
from dotenv import load_dotenv
from . import db

import os

load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

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


if (__name__ == "__main__"):
    app.run()
