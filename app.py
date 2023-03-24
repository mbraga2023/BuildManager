import os

from cs50 import SQL
import pandas as pd
from flask import Flask, flash, redirect, render_template, request, session
from tempfile import mkdtemp

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

# Configure CS50 Library to use SQLite database

db = SQL("sqlite:///users.db")

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


@app.route("/report")
def report():
    """Show report"""
    transactions_db = db.execute ("SELECT * FROM residentes")
    return render_template("report.html", transactions = transactions_db)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template ("register.html")

    else:
        nome = request.form.get("nome")
        sobrenome = request.form.get("sobrenome")
        email = request.form.get("email")
        phone = request.form.get("phone")
        unit = request.form.get("unit")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        try:
            new_user = db.execute("INSERT INTO residentes (nome, sobrenome, email, phone, unit, password ) VALUES (?, ?, ?, ?, ?, ?)", nome, sobrenome, email, phone, unit, password)
        except:
            return print("username already exists")

        return redirect("/")

