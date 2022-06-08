#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 15:55:54 2022

@author: linxiangling
"""

from flask import Blueprint, render_template

index_web=Blueprint('index_web', __name__)

@index_web.route("/index")
def index():
    return render_template("index.html")
