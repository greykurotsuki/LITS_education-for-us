#!/usr/bin/env python

import sys
import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/fs') # file system
def fs_scan():
    return 'FS'

if __name__ == '__main__':
    app.run()
