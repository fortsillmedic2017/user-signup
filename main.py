from flask import Flask, render_template, url_for, redirect,flash,request
from forms import UserSignup, UserLogin
import cgi

app = Flask(__name__)
app.config["DEBUG"] =True
app.config["SECRET_KEY"] = "a7d473df2aa95f2e786acae2b1024afd"
#>>> import secrets
#>>> secrets.token_hex(16)


# This just displays the empyty form on root/index page-->
@app.route("/")
def index():
    form  = UserSignup()
    return render_template("/signup.html", form=form, title="Signup")



@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = UserSignup()

    if form.validate_on_submit():
        return render_template("welcome.html", form=form, title="Welcome")
    return render_template("signup.html", form=form, title="Signup")
  

@app.route("/welcome")
def welcome():
    form = UserSignup()
    if form.validate_on_submit():
        return render_template("welcome.html", form=form, title="Welcome")
    return render_template("signup.html", form=form, title="Signup")
  

app.run()
