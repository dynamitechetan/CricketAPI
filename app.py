from flask import Flask, jsonify, request
import requests
import json
import sys
from bs4 import BeautifulSoup
from cricbuzz import Cricbuzz

app = Flask(__name__)

@app.route('/getMatches')
def getMatches():
    c = Cricbuzz()
    list =  c.matches()
    return jsonify(results=list)

@app.route('/liveScore')
def getMatchInfo():
    matchId = request.args.get('matchId')
    c = Cricbuzz()
    list =  c.livescore(matchId)
    return jsonify(results=list)

@app.route('/scorecard')
def scorecard():
    matchId = request.args.get('matchId')
    c = Cricbuzz()
    list = c.scorecard(matchId)
    return jsonify(results=list)

@app.route('/commentary')
def commentary():
    matchId = request.args.get('matchId')
    c = Cricbuzz()
    list = c.commentary(matchId)
    return jsonify(results=list)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)