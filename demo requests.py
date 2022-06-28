#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:32:06 2022

@author: peter
"""

import requests


city = 'Licata'

url  = 'http://api.openweathermap.org/data/2.5/weather'
url += '?appid=d1526a9039658a6f76950cff21823aff'
url += '&units=metric'
url += '&mode=json'
url += '&lang=en'
url += '&q=' + city

#print(url)

r = requests.get(url)

print(r.status_code)

if r.status_code == 200:
    #print(r.text)
    
    d = r.json()
    
    temperature = d['main']['temp']
    description = d['weather'][0]['description']
    
    print(f'In {city} it is now {temperature:.0f} degrees and {description}')
    
else:
    print(f'Status code {r.status_code}')
    