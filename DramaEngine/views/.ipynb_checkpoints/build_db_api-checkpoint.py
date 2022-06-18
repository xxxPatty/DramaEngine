#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 09:14:42 2022

@author: linxiangling
"""

import requests 
import json
import flask
from flask import request, Blueprint, jsonify
from models import buildDB

build_db_api=Blueprint('build_db_api', __name__)

@build_db_api.route('build_db', methods=['get'])
def build_db():
    buildDB.buildDB()
    return jsonify({"result":"Build DB sucess."})

@build_db_api.route('delete_stop_words', methods=['get'])
def delete_stop_words():
    buildDB.delete_stop_words_model()
    return jsonify({"result":"Delete stop words sucess."})