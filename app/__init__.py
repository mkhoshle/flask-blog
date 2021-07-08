from flask import Flask, request, render_template
from dotenv import load_dotenv
from . import db

import os

load_dotenv()
app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
db.init_app(app)

if (__name__ == "__main__"):
    app.run(debug=True)
