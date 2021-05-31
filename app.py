from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)
app.config["SECRET_KEY"] = "my-little-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def homepage():
    """ homepage listing pets """
    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)