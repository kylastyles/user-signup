from flask import Flask, request, render_template, redirect, url_for
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/', methods=["GET", "POST"])
def validate():

    username = request.form["username"]
    username_error = ""

    if " " in username == True:
        username_error = "No spaces allowed in Username field."
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters."
    else:
        username_error = ""

    password1 = request.form["password1"]
    password1_error = ""

    if " " in password1:
        password1_error = "No spaces allowed in passwords."
    elif len(password1) < 3 or len(password1) > 20:
        password1_error = "Password must be between 3 and 20 characters."
    else:
        password1_error = ""

    password2 = request.form["password2"]
    password2_error = ""

    if password1 != password2:
        password2_error = "Passwords must match."
    else:
        password2_error = ""

    email = request.form["email"]
    email_error = ""

    if email != "":
        if "@" not in email or "." not in email or " " in email:
            email_error = "Please enter a valid email. (Optional)"
        elif len(email) < 3 or len(email) > 20:
            email_error = "Email may not be less than 3 or greater than 20 characters."
    else:
        email_error = ""

    if not username_error and not password1_error and not password2_error and not email_error:
        return redirect(url_for("welcome", username=username))
    else:
        return render_template("index.html", username = username, username_error = username_error, password1_error = password1_error, password2_error = password2_error, email = email, email_error = email_error)




@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", username = username)


app.run()