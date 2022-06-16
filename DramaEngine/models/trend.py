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

from pymongo import MongoClient
import datetime
from dateutil.relativedelta import relativedelta

from opencc import OpenCC

#本月
#本季
#今年
#前n年
def get_trend(method, year):
    #連線 mongodb
    client = MongoClient('mongodb+srv://Patty:patty_881114@sandbox.lbkac.mongodb.net/test')
    db = client.DramaEngine
    movies = db.MovieInfo
    '''
    data = movies.find()
    for movie in data:
        print("原本:")
        print(movie['_id'])
        print(datetime.strptime(movie['release_date'], "%Y-%m-%d"))
        movies.update_one({"_id": movie['_id']}, {"$set" : {"release_datetime":datetime.strptime(movie['release_date'], "%Y-%m-%d")}})
    '''
    #拿到指定時間內的電影完整資訊
    geners = [] #電影類型
    keywords = [] #電影關鍵字（包含自己抓的＆原本的，db裡的是已經包含兩個的！）
    
    #抓出指定時間內 電影的所有類型、關鍵字
    today = datetime.datetime.today()
    if method=="month":
        start = today + relativedelta(months=-1)
    elif method=="quarter":
        start = today + relativedelta(months=-3)
    elif method=="year":
        start = today + relativedelta(years=-1)
    else:
        start = today + relativedelta(years=-int(year))
    
    #data = movies.find({"date":{$gte:"2022-01-01",$lte:"2022-12-31"}})
    data = movies.find({"$and":[{'release_datetime': {'$gte': start}}, {'release_datetime': {'$lte': today}}]})
    
    #拿到 generId 跟 generName 的對應
    url = "https://api.themoviedb.org/3/genre/movie/list"
    gener_id_to_name = {}
    querystring = {"api_key":"caba0bd5cf43c08405f1e55ef4c591a7", "language":"zh-TW"}
    response = requests.request("GET", url, params=querystring)
    cc = OpenCC('s2t')
    for gener in response.json()['genres']:
        gener_id_to_name[gener['id']] = cc.convert(gener['name'])
    
    #統計電影的類型、關鍵字出現次數
    trend = {}
    trend['gener'] = {}
    trend['keywords'] = {}
    #print("電影: ")
    for movie in data:
        #print("電影名稱: "+movie['title'])
        #print("上映日期: "+movie['release_date'])
        #print("----------")
        
        for gener in movie['genre_ids']:
            if gener_id_to_name[gener] not in trend['gener']:
                trend['gener'][gener_id_to_name[gener]] = 1
            else:
                trend['gener'][gener_id_to_name[gener]] += 1
        
        for key in movie['keywords']:
            if key not in trend['keywords']:
                trend['keywords'][key] = 1
            else:
                trend['keywords'][key] += 1
    #trend['gener'] = sorted(trend['gener'].items(), key=lambda x: x[1], reverse=True)
    #trend['keywords'] = sorted(trend['keywords'].items(), key=lambda x: x[1], reverse=True)
    '''
    for g in trend['gener']:
        print(g[0] + " - " + str(g[1]))
    ''' 
    return trend