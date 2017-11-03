from app import app
from flask import render_template

@app.route("/")
@app.route("/signin")
def home_page():
    return render_template("index.html")

@app.route("/register")
def register_user():
    return render_template("register.html")