#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:52:43 2022

@author: linxiangling
"""

from flask import Flask
from flask import render_template
from views import register_blueprint
from flask_cors import CORS
import models
from views import register_blueprint


# @app.route("/")
# def hello():
#     return render_template('index.html')
def create_app():
    app = Flask(__name__)
    app.jinja_env.auto_reload = True
    CORS(app)
    # register app
    register_blueprint(app)
    return app
    
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")

    
