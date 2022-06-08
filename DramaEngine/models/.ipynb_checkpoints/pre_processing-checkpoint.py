#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 22:08:43 2022

@author: cihcih
"""

import requests
import json
import jieba
from jieba import analyse
from googletrans import Translator
import re


def get_all_gener():
    url = "https://api.themoviedb.org/3/genre/movie/list"
    geners = []
    querystring = {"api_key":"0f79586eb9d92afa2b7266f7928b055c", "language":"zh-TW"}
    response = requests.request("GET", url, params=querystring)
    geners.extend(response.json()["genres"])
    
    return geners