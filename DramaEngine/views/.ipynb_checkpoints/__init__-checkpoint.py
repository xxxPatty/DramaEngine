#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:05:37 2022

@author: linxiangling
"""

from .index_web import index_web
from .search_api import search_api
from .trend_api import trend_api
from .favorite_movie_api import favorite_movie_api

blueprint_prefix = [(search_api, ""), (index_web, ""), (trend_api, ""), (favorite_movie_api, "")]

def register_blueprint(app):
    for blueprint, prefix in blueprint_prefix:
        app.register_blueprint(blueprint, url_prefix=prefix)
    return app
