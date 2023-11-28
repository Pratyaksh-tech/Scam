from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from App import app

@app.route('/', methods=["GET", "POST"])
def home():
	return render_template("home.html")
