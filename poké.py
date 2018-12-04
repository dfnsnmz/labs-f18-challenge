#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:02:44 2018

@author: defnesonmez
"""

import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
query = input("Please enter a pokemon ID or name \n")

if(query.isnumeric()):
    query_url = BASE_URL + query + "/"
    raw_html = requests.get(query_url, stream=True).content
    data = json.loads(raw_html)
    print("The pokemon with id", query, "is", data["name"])

else:
    #searching for a name
    query = query.lower()
    query_url = BASE_URL + query + "/"
    raw_html = requests.get(query_url, stream=True).content
    data = json.loads(raw_html)
    print(query, "has id", data["id"])
