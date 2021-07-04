from flask import Flask
from dotenv import load_dotenv
from app import views
load_dotenv()
app = Flask(__name__)

from app import routes

# app.add_url_rule('/', view_func=views.index)
# app.add_url_rule('/about', view_func=views.about)
# app.add_url_rule('/blog', view_func=views.blog)
# app.add_url_rule('/portfolio', view_func=views.portfolio)
# app.add_url_rule('/cv', view_func=views.cv)

if (__name__ == "__main__"):
    app.run(debug=True)