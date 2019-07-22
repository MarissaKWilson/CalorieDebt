#!/usr/bin/env python
"""
dao/foodDAO.py
"""

import requests
import json
import CalorieDebtConstants

# Parameter	Required	Default	Description
# api_key	y	        n/a	    Must be a data.gov registered API key
# ndbno	    y	        n/a	    NDB no
# type	    n	        b       Report type: [b]asic or [f]ull or [s]tats
# format1	n	        JSON	Report format: xml or json

def searchById (id, type = 'b'):
    data = {}
    data['api_key'] = CalorieDebtConstants.API_KEY
    data['nbno'] = id
    data['type'] = type
    response = requests.post(CalorieDebtConstants.USDA_URL, data=data)
    return response


# Parameter	Required	Default	Description
# api_key	y	        n/a	    Must be a data.gov registered API key
# q	        n	        ""	    Search terms
# ds	    n	        ""	    Data source. Must be either 'Branded Food Products' or 'Standard Reference'
# fg	    n	        ""	    Food group ID
# sort	    n	        r	    Sort the results by food name (n) or by search relevance (r)
# max	    n	        50	    maximum rows to return
# offset	n	        0	    beginning row in the result set to begin
# format1	n	        JSON 	results format: json or xml
def searchByName (name):
    data = {}
    data['api_key'] = CalorieDebtConstants.API_KEY
    data['q'] = name
    response = requests.post(CalorieDebtConstants.USDA_URL, data=data)
    return response

def searchByFoodGroup (foodgroupID):
    data = {}
    data['api_key'] = CalorieDebtConstants.API_KEY
    data['fg'] = foodgroupID
    response = requests.post(CalorieDebtConstants.USDA_URL, data=data)
    return response
