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
    user_genres = data['user_genres']     #類型list
    user_description = data['user_description']     #描述string
    user_keywords = data['user_keywords']
    result = search.search_by_description_model(user_genres, user_description, user_keywords)
    return jsonify({"result":result})


