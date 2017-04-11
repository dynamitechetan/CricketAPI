# data conversion, the headers for the response, etc
from flask import Flask, jsonify, request
import requests
import json
import sys
from bs4 import BeautifulSoup
from cricbuzz import Cricbuzz

# Initialize the Flask application
app = Flask(__name__)
app.run(debug=True)

# This route will return a list in JSON format
@app.route('/getMatches')
def getMatches():
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    c = Cricbuzz()
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    list =  c.matches()
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return jsonify(results=list)

@app.route('/liveScore')
def getMatchInfo():
    matchId = request.args.get('matchId')
    c = Cricbuzz()
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    list =  c.livescore(matchId)
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return jsonify(results=list)



if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("1234")
    )


