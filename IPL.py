# data conversion, the headers for the response, etc
from flask import Flask, jsonify
import requests
import json
import sys
from bs4 import BeautifulSoup
from cric import Cricbuzz

# Initialize the Flask application
app = Flask(__name__)


# This route will return a list in JSON format
@app.route('/')
def index():
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    c = Cricbuzz()
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    list =  c.matches()
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return jsonify(results=list)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("1234")
    )


