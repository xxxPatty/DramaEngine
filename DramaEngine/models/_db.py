#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:54:12 2022

@author: linxiangling
"""

from pymongo import MongoClient

DB = MongoClient('mongodb+srv://Patty:patty_881114@sandbox.lbkac.mongodb.net/test')['DramaEngine']

MovieInfo_COLLECTION = DB['MovieInfo']
