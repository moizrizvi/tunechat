#!/bin/python

import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home(**kwargs):
    return render_template('index.html')

@app.route('/play')
def play(**kwargs):
    return render_template('play.html')

def get_server():
    return app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
