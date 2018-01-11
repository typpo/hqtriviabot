#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import json

from flask import Flask
from flask import request
from flask import jsonify

from quotes import QUOTES

app = Flask(__name__)
app.debug = True

def get_resp(text):
    quote = random.choice(QUOTES)
    return {'text': 'Tip: %s' % (quote)}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        req = get_resp(text)
        return jsonify(**req)
    elif request.method == 'GET':
        return jsonify(get_resp(''))


if __name__ == '__main__':
    app.run(port=4243)
