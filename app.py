from flask import Flask, request
from random import randint

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World"

@app.route("/nums")
def get_nums():
    limit: int = request.args.get('limit', default=10, type=int)
    return [randint(0, 1000) for _ in range(limit)]


"""
IMPORTANT
Make sure this file is named app.py
Run in terminal by calling 'flask run'
"""
