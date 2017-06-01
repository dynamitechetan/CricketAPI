# CricketAPI
-----------------------------------------------------------------------------------------------------------
					Cricket API - Live Scores | Commentary | ScoreCard
-----------------------------------------------------------------------------------------------------------
CricketAPI aims to provide free access to all cricket matches via API for all ODIs, Tests & T20s (International and IPL). 
## It includes following features:
- Scorecards of matches 
- Ball by Ball Commentary
- Live Scores

# Usage
- getAllMatches <br>
   ```http://localhost:1234/getMatches``` 
   <br>
This endpoint will return list of all Live and Upcoming matches. <br>

- liveScore <br>
   ```http://localhost:1234/livescore?matchId={matchID}``` 
   <br>
This endpoint will return live scores of {matchID}. <br>

- scorecard <br>
   ```http://localhost:1234/scorecard?matchId={matchID}``` 
   <br>
This endpoint will return scorecard of {matchId}. <br>


- getAllMatches <br>
   ```http://localhost:1234/commentary?matchId={matchID}``` 
   <br>
This endpoint will return ball by ball commentary of {matchID}. <br>

# Running and Setup
  Tested on python 2.7 <br>
  ```pip install -r requirements.txt``` <br>
  ```python server.py```
# Heroku
  ```http://cricketapi.herokuapp.com/{endpoint}```<br>
  eg. ```http://cricketapi.herokuapp.com/getMatches```
