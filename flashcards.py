from datetime import datetime
from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Weloclome to the flask application"

@app.route("/date")
def dateTime():
    return "The time now is "+ str(datetime.now())