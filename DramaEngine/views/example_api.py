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


example_api=Blueprint('example_api', __name__)
@example_api.route('example')
def example():
    return jsonify({"message":"this is an example api"})