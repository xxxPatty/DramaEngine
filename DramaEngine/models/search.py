#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 10:45:22 2022

@author: linxiangling
"""

import requests
import json
import jieba
from jieba import analyse
from googletrans import Translator
import re


def search_by_description_model(tv_or_movie, genres_ids, user_description):
    # #TV(0) or Movie(1)
    # tv_or_movie = 1
    
    # #使用者選的類型
    # # genres_ids = [16, 10759]
    # # genres_ids = [10759, 16, 35]
    # # genres_ids = [28, 80, 12]
    # # genres_ids = [35, 10402]
    # # genres_ids = [28, 12, 878]
    # genres_ids = [16, 35, 14, 10402]
    
    genres_id_strs = ""
    for genres_id in genres_ids:
        genres_id_strs += str(genres_id) + ","
    genres_id_strs = genres_id_strs[:-1]
    
    # #使用者的描述
    # # user_description = "主角鳴人體內封印著九尾妖狐，因此從小被排擠。為了獲得其他人的認同，夢想當上火影。"
    # # user_description = "間諜爸爸、殺手媽媽、讀心術小孩組成家庭的爆笑故事。"
    # # user_description = "間諜在裁縫店上班。"
    # # user_description = "音樂劇作品，女主角夢想成為音樂製作人，對唱歌很有天賦，陰錯陽差下加入阿卡貝拉樂團，幫助樂團茁壯成長成了新目標。"
    # # user_description = "反烏托邦作品，人們生活在牆中與外界隔離，主角一行人為了逃出去要突破移動迷宮的層層關卡。"
    # user_description = "音樂劇。生在魔法世界中的名望大家族，唯獨女主角沒有魔力，但他心地善良，是家族中聯繫的重要人物。某天，她發現他們住的魔法屋出現異常，魔力一天天減弱，為了阻止事態更嚴重，女主角開始行動搶救。"
    
    
    #拿到相關電影資訊前20*n筆
    if tv_or_movie == 0:
        url = "https://api.themoviedb.org/3/discover/tv"
    else:
        url = "https://api.themoviedb.org/3/discover/movie"
    
    related_movies = []
    for i in range(1, 2):   
        querystring = {"api_key":"f53d31e8101decd04ef4135886d2db17", "language":"zh-TW","sort_by":"popularity.desc","include_adult":"true","include_video":"true","page":str(i),"with_watch_monetization_types":"flatrate","with_genres":genres_id_strs}
        response = requests.request("GET", url, params=querystring)
        related_movies.extend(response.json()["results"])
    
    #print(related_movies)
    
    #分析movie overview關鍵字
    #tf-idf
    for movie in related_movies:
        movie["overview"] = movie["overview"].replace(".", " ")
        #default回傳前20名
        tags = jieba.analyse.extract_tags(movie["overview"])
        movie["keywords"] = tags
        #print(tags)
    
    
        
    translator = Translator()
    #拿到movie既有keywords
    if tv_or_movie == 0:
        for movie in related_movies:
            movie_id = str(movie["id"])
            
            url2 = "https://api.themoviedb.org/3/tv/" + movie_id + "/keywords?api_key=f53d31e8101decd04ef4135886d2db17"
            response = requests.request("GET", url2)
            #print(response.text)
            keywords_from_api = [keyword["name"] for keyword in response.json()["results"]]
            translated_keywords = [translator.translate(word, dest='zh-tw').text for word in keywords_from_api]
            movie["keywords"].extend(translated_keywords)
            #將title斷詞再加入當keywords
            title_seg_list = jieba.cut(movie["name"])
            movie["keywords"].extend(title_seg_list)
    else:
        for movie in related_movies:
            movie_id = str(movie["id"])
            
            url2 = "https://api.themoviedb.org/3/movie/" + movie_id + "/keywords?api_key=f53d31e8101decd04ef4135886d2db17"
            response = requests.request("GET", url2)
            #print(response.text)
            keywords_from_api = [keyword["name"] for keyword in response.json()["keywords"]]
            translated_keywords = [translator.translate(word, dest='zh-tw').text for word in keywords_from_api]
            movie["keywords"].extend(translated_keywords)
            #將title斷詞再加入當keywords
            title_seg_list = jieba.cut(movie["title"])
            movie["keywords"].extend(title_seg_list)
        
    #算分與排名
    output_movies = []
    for movie in related_movies:
        search = re.findall(r"(?=("+'|'.join(movie["keywords"])+r"))", user_description)
        scores = len(search)
        movie["scores"] = scores
        if search != []:
            output_movies.append(movie)
        
    sorted_oupput_movies = sorted(output_movies, key=lambda d:d["scores"], reverse=True)
    
    #print(sorted_oupput_movies)
    if tv_or_movie == 0:
        for result in sorted_oupput_movies:
            print(result["name"])
    else:
        for result in sorted_oupput_movies:
            print(result["title"])
        
    return sorted_oupput_movies
        
    
