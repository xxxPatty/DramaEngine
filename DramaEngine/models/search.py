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


def search_by_description_model(genres, user_description):  #!!!要多欄位給使用者選嗎？
    all_db_movie = [{'id': i['id'], 'title': i['title'], 'keywords': i['keywords'], 'genre_ids': i['genre_ids'], 'backdrop_path': i['backdrop_path']} for i in _db.MovieInfo_COLLECTION.find()]
    #算分與排名
    output_movies = []
    for movie in all_db_movie:
        search = re.findall(r"(?=("+'|'.join(movie["keywords"])+r"))", user_description)
        scores = len(search)
        movie["scores"] = scores
        if search != []:
            output_movies.append(movie)
        
    sorted_oupput_movies = sorted(output_movies, key=lambda d:d["scores"], reverse=True)
    
    #print(sorted_oupput_movies)
    
    for result in sorted_oupput_movies:
        print(result["title"])
        
    return sorted_oupput_movies
        
    
