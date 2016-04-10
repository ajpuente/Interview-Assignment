#!/usr/bin/python
from flask import Flask, jsonify
app = Flask(__name__)

dict = {'id': 1, 'name': 'Limelight'}


@app.route('/')
def dict_json():
    return jsonify(**dict)

if __name__ == '__main__':
    app.run()

