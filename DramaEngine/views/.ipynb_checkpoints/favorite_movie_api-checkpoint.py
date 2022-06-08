#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 22:07:59 2022

@author: cihcih
"""
from pymongo import MongoClient

import requests 
import json
import flask
from flask import request, Blueprint, jsonify
from models import favorite_movie
from bson.json_util import dumps
import bson.json_util as json_util


favorite_movie_api=Blueprint('favorite_movie_api', __name__)

@favorite_movie_api.route('get_my_favorite', methods=['post'])
def search_by_description():
    data = request.get_json()
    movie_id = data['movie_id']
    data = favorite_movie.get_my_favorite(movie_id)
    #print(data)
    
    return jsonify({"data": json.loads(json_util.dumps(data))})