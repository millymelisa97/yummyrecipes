from app import app
from flask import render_template, request, redirect, url_for
from app.models import User


@app.route("/")
@app.route("/signin")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    # display form if user hasnot submitted any data
    if not request.form:
        return render_template("register.html")

    # validate user data
    data = request.form
    errors = []
    if len(data["username"]) < 5 and len(data["username"]) > 20:
        errors.append("Username must be between 5 and 20 characters")
    if len(data["password"]) < 8:
        errors.append("Password should be a atleast 8 characters")
    if data["password"] != data["confirm_password"]:
        errors.append("Passwords don't match")
    if str(data["username"]) in User.all_users:
        errors.append("Username '{}' is already in use".format(data["username"]))

    if not errors:
        # register the user
        user = User(data["username"], data["password"])
        # redirect user to the hone page
        return redirect(url_for("home"))

    return render_template("register.html", errors=errors, data=data)
