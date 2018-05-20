from flask import Flask, jsonify, request
import json
import os


app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Block-a-Bed"

if __name__=='__main__':
    #App takes approx 20-30s without threaded=True to return async reponse.
    app.run(debug=True, threaded=True)