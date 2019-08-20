#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:49:27 2018

@author: roopal
"""

BP = int(input('enter BP:',))

if BP < 80 :
    print('bp is low' )
elif 80<= BP  <=120:
    print('BP is normal')
elif BP > 120:
    print("bp is high")
temp = int(input('enter temp:',))
if temp < 80 :
    print('temp is low' )
elif 80<=  temp  <=102:
    print('temp is normal')
elif temp > 102:
    print("temp is high")    
    
    