import requests
import json
import jieba
from jieba import analyse
from googletrans import Translator
import re

from pymongo import MongoClient

def get_my_favorite(movie_id):
    
    #連線 mongodb
    client = MongoClient('mongodb+srv://Patty:patty_881114@sandbox.lbkac.mongodb.net/test')
    db = client.DramaEngine
    movies = db.MovieInfo
    
    #拿到最愛電影的完整資訊
    favorites = [] #完整電影資訊
    gener = [] #電影類型
    keywords = [] #電影關鍵字（包含自己抓的＆原本的，db裡的是已經包含兩個的！）
    
    #抓出最愛電影的所有類型、關鍵字
    print("最愛電影: ")
    for myId in movie_id:
        myQuery = { "id": myId }
        #print("找到的結果: ")
        #print(movies.find(myQuery)[0]["keywords"])
        temp = movies.find(myQuery)[0]
        gener.extend(temp["genre_ids"])
        keywords.extend(temp["keywords"])
        favorites.append(temp["id"])
        print(temp["title"])
        
    print("----------")
    #跟其他電影比較，算分＆排名
    print("推薦電影: ")
    cursor = movies.find({}) #DB中的所有電影
    output_movies = []
    output_movies_id = []
    for movie in cursor:
        result_gener = [g for g in gener if g in movie["genre_ids"]]
        result_keywords = [k for k in keywords if k in movie["keywords"]]
        movie["scores"] = len(result_gener) + len(result_keywords)
        if movie["scores"] != 0 and movie["id"] not in output_movies_id and movie["id"] not in favorites:
            output_movies.append(movie)
            output_movies_id.append(movie["id"])
            
    sorted_output_movies = sorted(output_movies, key=lambda d:d["scores"], reverse=True)[0:10] #取前10名
    for recommand in sorted_output_movies:
        print(recommand["title"])
        #print(recommand["title"] + " " + str(recommand["scores"]))
    
    return sorted_output_movies