#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:52:43 2022

@author: linxiangling
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)
# @app.route("/")
# def hello():
#     return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")

    
