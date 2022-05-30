#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 10:45:22 2022

@author: linxiangling
"""

import requests
import json
import re
from . import _db
from opencc import OpenCC


def search_by_description_model(user_genres, user_description):  #!!!要多欄位給使用者選嗎？
    all_db_movie = [{'id': i['id'], 'title': i['title'], 'keywords': i['keywords'], 'genre_ids': i['genre_ids'], 'backdrop_path': i['backdrop_path']} for i in _db.MovieInfo_COLLECTION.find()]
    
    api_key = "f53d31e8101decd04ef4135886d2db17"
    genre_url = "https://api.themoviedb.org/3/genre/movie/list?api_key="+api_key+"&language=zh-TW"
    genre_list = requests.request("GET", genre_url).json()['genres']
    genre_dict = {}
    #簡轉繁
    cc = OpenCC('s2tw')
    for i in genre_list:
        genre_dict[i['id']] = cc.convert(i['name'])
        
    #算分與排名
    output_movies = []
    for movie in all_db_movie:
        #print(movie)
        #genre_ids轉為name
        movie['genres'] = []
        for genre in movie['genre_ids']:
            movie['genres'].append(genre_dict[genre])
        #用正則表達式比對使用者描述與關鍵字計分
        search = re.findall(r"(?=("+'|'.join(movie["keywords"])+r"))", user_description)
        scores = len(search)
        movie["scores"] = scores
        #若使用者類型與電影類型匹配，每個加兩分
        for user_genre in user_genres:
            if user_genre in movie['genres']:
                movie["scores"] += 2
        if search != []:
            output_movies.append(movie)
        
    sorted_oupput_movies = sorted(output_movies, key=lambda d:d["scores"], reverse=True)
    
    #print(sorted_oupput_movies)
    
    for result in sorted_oupput_movies[0:20]:
        print(result["title"])
        print(result["scoress"])
        
    return sorted_oupput_movies
        
    
