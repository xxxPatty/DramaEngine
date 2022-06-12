#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 22:07:59 2022

@author: cihcih
"""

import requests 
import json
import flask
from flask import request, Blueprint, jsonify
from models import trend
from bson.json_util import dumps
import bson.json_util as json_util

trend_api=Blueprint('trend_api', __name__)

'''
{
    "method":"years",
    "years": "2"
}
'''
@trend_api.route('trend', methods=['post'])
def get_trend():
    para = request.get_json()
    method = para['method']
    year = para['years']
    data = trend.get_trend(method,year)
    
    #print(data)
    
    return jsonify({"data": json.loads(json_util.dumps(data))})