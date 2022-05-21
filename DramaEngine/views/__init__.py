#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:05:37 2022

@author: linxiangling
"""

from .index_web import index_web
from .example_api import example_api

blueprint_prefix = [(example_api, "/api")]

def register_blueprint(app):
    for blueprint, prefix in blueprint_prefix:
        app.register_blueprint(blueprint, url_prefix=prefix)
    return app
