from http import server
from flask import Flask, render_template, redirect
from flask.helpers import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm


from dash_application import create_dash_application



application = Flask(__name__)
#flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
Bootstrap(application)
#db = SQLAlchemy(flask_app)
#migrate = Migrate(flask_app, db)
create_dash_application(application)


@application.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    application.run(port=5000, debug=True)
