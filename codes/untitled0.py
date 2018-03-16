# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:55:09 2018

@author: yuchen
"""
import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
gooddata=list()

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

   # url = urllib.parse.urlencode({'address': address})
    print('Retrieving', address)
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print(data.decode())
    tree = ET.fromstring(data)
#    gooddata.append(data.decode())
#    
#
#    info = json.loads(data)
#    sum1=list()
#    #i=0
#    for item in info:
#        #sum1.append(item['comments']["count"])
#        for i in range(0,50):
#            print(item["comments"][i]["count"])
#            sum1.append(item["comments"][i]["count"])        
#    
#     #   i=i+1     http://py4e-data.dr-chuck.net/comments_26585.json
#    print(sum(sum1))
    
    
 #   for item in gooddata:
        