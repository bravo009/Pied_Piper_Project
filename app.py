#! /usr/bin/python
import time
import os
from flask import Flask
import redis

r = redis.Redis(host='', port='', password='')

app = Flask(__name__)

PIval = 0 # distance value

@app.route('/')
def mainmenu():
    global r
    PIval = r.get('RPIvalue')

    return """
    <html><body>
    <center><h1>BETA version of my Parking automation system<br/>
        <h2><u>Parking lot status : {0}<br>
    </center>
    </body></html>
    """.format(PIval)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
