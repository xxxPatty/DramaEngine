#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:58:46 2022

@author: linxiangling
"""

import requests
import json
from . import _db
import jieba
from jieba import analyse
from googletrans import Translator


def buildDB():      
    api_key = "f53d31e8101decd04ef4135886d2db17"
    
    all_db_movie_ids = [i['id'] for i in _db.MovieInfo_COLLECTION.find()]

    query_movie_by_genre_url = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&language=zh-TW&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate&release_date.gte=2000-01-01"
    response = requests.request("GET", query_movie_by_genre_url)
    
    all_movies = response.json()["results"]
    total_pages = response.json()["total_pages"]
    
    
    translator = Translator()
    for page in range(1, total_pages+1):#
        query_movie_by_page_url = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&language=zh-TW&sort_by=popularity.desc&include_adult=false&include_video=false&page="+str(page)+"&with_watch_monetization_types=flatrate&&release_date.gte=2000-01-01"
        response = requests.request("GET", query_movie_by_page_url)
        for movie in response.json()["results"]:
            if movie["id"] not in all_db_movie_ids:
                all_movies.append(movie)
                #分析overview取出關鍵字
                #tf-idf
                movie["overview"] = movie["overview"].replace(".", " ")
                #default回傳前20名
                tags = jieba.analyse.extract_tags(movie["overview"])
                movie["keywords"] = tags
                
                #拿到所有電影各自的既有關鍵字並翻譯
                query_keywords_url = "https://api.themoviedb.org/3/movie/"+str(movie["id"])+"/keywords?api_key="+api_key
                query_keywords_response = requests.request("GET", query_keywords_url)
                
                keywords_from_api = [keyword["name"] for keyword in query_keywords_response.json()["keywords"]]
                trans_keyword = [translator.translate(word, dest='zh-tw').text for word in keywords_from_api]
                movie["keywords"].extend(trans_keyword)
                #將title斷詞再加入當keywords
                title_seg2 = []
                title_seg_list = jieba.cut(movie["title"])
                for word in title_seg_list:
                    if word != " " and word != "!" and word != "," and word != "." and word != "-" and word != ":" and word != "'" and word != "！" and word != "，" and word != "。" and word != "－" and word != "_" and word != "＿" and word != "…" and word != "：" and word != "(" and word != ")" and word != "（" and word != "）" and word != "＆":
                        title_seg2.append(word)
                movie["keywords"].extend(title_seg2)
                #存入DB  
                _db.MovieInfo_COLLECTION.insert_one(movie)
                
                print("save")
                print(movie)
        
    
        
    