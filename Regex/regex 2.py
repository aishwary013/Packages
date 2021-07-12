# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:19:06 2020

@author: aishwary
"""


from os import chdir
chdir('G:/My Drive/2020/Coding/Regex')
import re

pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

with open('data.txt','r',encoding='utf-8') as f:
    contents=f.read()
    matches=pattern.finditer(contents)
    for match in matches:
        print(match)
        
# character set uses square brackets to match characters we want
        
pattern=re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

with open('data.txt','r',encoding='utf-8') as f:
    contents=f.read()
    matches=pattern.finditer(contents)
    for match in matches:
        print(match)

