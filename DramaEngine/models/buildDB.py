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
import re
#r"\",
stop_words = [" ", "!", ",", ".", "-", ":", "'", "！", "，", "。", "－", "一", "_", "＿", "…", "：", "(",  ")", "（", "）", "＆", "¿", "?", "*", "．", "·", "~", "...", "+", "、", "/", "我", "是", "她", "他", "他們", "我們","的", "上", "與", "一個", "一名", "女主角", "男主角", "主角", "之", "人", "小", "大","這個", "在", "來", "人們", "人類", "成為", "透過", "版", "他的", "發現", "原來","自己", "想要", "決定", "開始", "其中", "因為", "喜歡", "應該", "為", "這次", "吧", 'ン','ー','Go','&','in','the','A','ç','The','of','La','Ni','ñ','a','Gun','の','No','s','Nothing','de','Up','We','for','о','р','In','All','Film','్','at','প','া','য','ു','du','Le','い','and','Me','ó','Live','Vai','os','Last','Ever','오','н','е','а','к','л','e','Big','la','l','You','World','м','т','on','и','Is','to','Win','pi','ù','bello','C','est','M','é','m','En','es','S','O','pel','í','cula','El','el','y','New','One','House','Part','ร','น','o','Family','á','Un','City','L','del', 'by','en','et','ä', 'भ','ल', '়', 'Т', 'ఫ', 'న', 'ക', 'റ', '്', 'ം', '"', 'А','ロ']
def buildDB():      
    api_key = "f53d31e8101decd04ef4135886d2db17"
    
    all_db_movie_ids = [i['id'] for i in _db.MovieInfo_COLLECTION.find()]

    query_movie_by_genre_url = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&language=zh-TW&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate&release_date.gte=2000-01-01"
    response = requests.request("GET", query_movie_by_genre_url)
    total_pages = response.json()["total_pages"]
    
    
    translator = Translator()
    for page in range(1, total_pages+1):#
        query_movie_by_page_url = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&language=zh-TW&sort_by=popularity.desc&include_adult=false&include_video=false&page="+str(page)+"&with_watch_monetization_types=flatrate&&release_date.gte=2000-01-01"
        response = requests.request("GET", query_movie_by_page_url)
        for movie in response.json()["results"]: 
            if movie["id"] not in all_db_movie_ids:
                #分析overview取出關鍵字
                #tf-idf
                movie["overview"] = movie["overview"].replace(".", " ")
                #default回傳前20名
                tags = jieba.analyse.extract_tags(movie["overview"])
                movie["keywords"] = []
                for word in tags:
                    if word not in stop_words:
                        movie["keywords"].append(word)
                
                #拿到所有電影各自的既有關鍵字並翻譯
                query_keywords_url = "https://api.themoviedb.org/3/movie/"+str(movie["id"])+"/keywords?api_key="+api_key
                query_keywords_response = requests.request("GET", query_keywords_url)
                
                keywords_from_api = [keyword["name"] for keyword in query_keywords_response.json()["keywords"]]
                trans_keyword = [translator.translate(word, dest='zh-tw').text for word in keywords_from_api]
                for word in trans_keyword:
                    if word not in stop_words:
                        movie["keywords"].append(word)
                #將title斷詞再加入當keywords
                title_seg2 = []
                title_seg_list = jieba.cut(movie["title"])
                for word in title_seg_list:
                    if word not in stop_words:
                        title_seg2.append(word)
                movie["keywords"].extend(title_seg2)
                #存入DB
                _db.MovieInfo_COLLECTION.insert_one(movie)
                
                print("save")
                print(movie)
                
def delete_stop_words_model():  
    all_db_movie = [{'id': i['id'], 'keywords': i['keywords']} for i in _db.MovieInfo_COLLECTION.find()]
    _db.MovieInfo_COLLECTION.update_many({}, {'$pull':{'keywords':{'$in':stop_words}}})
    regx = re.compile("^[0-9]", re.IGNORECASE)
    _db.MovieInfo_COLLECTION.update_many({}, {'$pull':{'keywords':regx}})

                
                
