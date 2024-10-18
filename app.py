import logging
import sys

import requests
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_HOST="https://api.formula1.com/6657193977244c13?d=account.formula1.com"

@app.route('/6657193977244c13', methods=["GET"])
def getjs():
    return requests.get("https://api.formula1.com/6657193977244c13").text

@app.route('/6657193977244c13', methods=["POST"])
def rewrite():
    app.logger.debug(request.headers)
    headers = {k:v for k,v in request.headers if k.lower() != 'host'}
    headers['Origin'] = "https://account.formula1.com"
    headers['Referer'] = "https://account.formula1.com/"
    res = requests.request(
        method          = "POST",
        url             = API_HOST,
        headers         = headers,
        data            = request.get_data(),
        cookies         = request.cookies,
        allow_redirects = False,
    )
    return res.text, res.status_code

if __name__ == "__main__":
    app.run()
