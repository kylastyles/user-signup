from flask import Flask, request, render_template, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def validate():

    username_entry = request.form["username"]
    username_error = ""

    if username_entry == "":
        username_error = "Please enter your username."
    elif " " in username_entry == True:
        username_error = "No spaces allowed in Username field."
    elif len(username_entry) < 3 or len(username_entry) > 20:
        username_error = "Username must be between 3 and 20 characters."
    else:
        username_error = ""

    password1_entry = request.form["password1"]
    password1_error = ""

    if password1_entry == "":
        password1_error = "Please enter your password."
    elif " " in password1_entry == True:
        password1_error = "No spaces allowed in Password field."
    elif len(password1_entry) < 3 or len(password1_entry) > 20:
        password1_error = "Password must be between 3 and 20 characters."
    else:
        password1_error = ""

    password2_entry = request.form["password2"]
    password2_error = ""

    if password2_entry == "":
        password2_error = "Please verify your password."
    elif password1_entry != password2_entry:
        password2_error = "Passwords must match."
    else:
        password2_error = ""

    email_entry = request.form["email"]
    email_error = ""

    if "@" not in email_entry or "." not in email_entry or " " in email_entry:
        email_error = "Please enter a valid email. (Optional)"
    elif len(email_entry) < 3 or len(email_entry) > 20:
        email_error = "Email may not be less than 3 or greater than 20 characters."
    else:
        email_error = ""

    #if not username_error and not password1_error and not password2_error and not email_error:
    return render_template("welcome.html", username_entry = username)
    #else:
    #    return render_template("index.html", username_error = username_error, password1_error = password1_error, password2_error = password2_error, email_error = email_error)

@app.route("/welcome", methods=["GET", "POST"])
def welcome(username_entry):
    #username = request.form["username"]
    return render_template("welcome.html", username_entry = username)


app.run()