#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:03:31 2022

@author: linxiangling
"""

import requests 
import json
import flask
from flask import request, Blueprint, jsonify
from models import search

search_api=Blueprint('search_api', __name__)

@search_api.route('search_by_description', methods=['post'])
def search_by_description():
    data = request.get_json()
    tv_or_movie = data['tv_or_movie']   #tv(0)還是movie(1)
    genres_ids = data['genres_ids']     #類型list
    user_description = data['user_description']     #描述string
    result = search.search_by_description_model(tv_or_movie, genres_ids, user_description)
    return jsonify({"result":result})
