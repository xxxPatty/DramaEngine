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
from models import pre_processing

pre_process_api=Blueprint('pre_process_api', __name__)

@pre_process_api.route('get_all_gener', methods=['get'])
def search_by_description():
    result = pre_processing.get_all_gener()
    return jsonify({"result":result})