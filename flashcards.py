from datetime import datetime
from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Weloclome to the flask application"

@app.route("/date")
def dateTime():
    return "The time now is "+ str(datetime.now())

counter=0

@app.route("/count_views")
def count_views():

    global counter
    counter+=1
    return "number of times this page is view is  "+ str(counter)

