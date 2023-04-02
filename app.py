import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, session, request
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required
import datetime


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database

db = SQL("sqlite:///banco.db")

# Make sure API key is set

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')
def index():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username_email = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/index")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/index")
@login_required
def dashboard():
    """Show dashboard"""
    user_id = session["user_id"]

    return render_template("index.html")


@app.route("/report")
def report():
    """Show report"""
    transactions_db = db.execute ("SELECT * FROM users")
    return render_template("report.html", transactions = transactions_db)

@app.route("/delete")
def delete():
    """delete row"""
    delete_db = db.execute ("SELECT * FROM users WHERE id = ?", delete_db[0]['id'])
    return render_template("report.html", transactions = delete_db)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register users"""
    if request.method == "GET":
        return render_template ("registeruser.html")

    else:
        nome = request.form.get("nome")
        sobrenome = request.form.get("sobrenome")
        username_email = request.form.get("username_email")
        phone = request.form.get("phone")
        unit = request.form.get("unit")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username_email:
            return apology("Must have a username")
        if not password:
            return apology("Must have password")
        if not confirmation:
            return apology ("Must have confirmation")
        if password != confirmation:
            return apology ("Password and confirmation does not match")
        
        hash = generate_password_hash(password)

        try:
            new_user = db.execute("INSERT INTO users (username_email, hash, nome, sobrenome, phone, unit) VALUES (?, ?, ?, ?, ?, ?)", username_email, hash, nome, sobrenome, phone, unit)
            flash("User registered")

        except:
             return apology("username already exists")

        session["user_id"] = new_user
        return redirect("/register")
    
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

