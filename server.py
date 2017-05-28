from flask import Flask, jsonify, request
import requests
import json
import sys
from bs4 import BeautifulSoup
from cricbuzz import Cricbuzz
from flask import Response
app = Flask(__name__)

@app.route('/getMatches')
def getMatches():
    c = Cricbuzz()
    list =  c.matches()
    return Response(json.dumps(list),  mimetype='application/json')

@app.route('/livescore')
def getMatchInfo():
    matchId = request.args.get('matchId')
    c = Cricbuzz()
    list =  c.livescore(matchId)
    return Response(json.dumps(list),  mimetype='application/json')

@app.route('/scorecard')
def scorecard():
    matchId = request.args.get('matchId')
    c = Cricbuzz()
    list = c.scorecard(matchId)
    return Response(json.dumps(list),  mimetype='application/json')

@app.route('/commentary')
def commentary():
    matchId = request.args.get('matchId')
    c = Cricbuzz()
    list = c.commentary(matchId)
    return Response(json.dumps(list),  mimetype='application/json')

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("1234")
    )


