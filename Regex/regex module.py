# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:22:38 2020

@author: aishwary
"""
from os import chdir
chdir('G:/My Drive/2020/Coding/Regex')

import re
print('\tTab')
print(r'\tTab')

# Variables
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
pat
mat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

def matches(pattern,text):
    matches=pattern.finditer(text)
    for match in matches:
        print(match)

# Search pattern
pattern=re.compile(r'abc')
matches(pattern,text_to_search)    

# search for period
pattern=re.compile(r'.')
matches(pattern,text_to_search)    

# prints everything as . is a special character
# to seacrh for period
pattern=re.compile(r'\.')
matches(pattern,text_to_search)    

# search a specific string
pattern=re.compile(r'coreyms.com')
matches(pattern,text_to_search)    

# Checking metacharacters
#\d - all digits, \D - Not a digit, \w - word character (a-z, A-Z, 0-9, _), \W - not a word character

pattern=re.compile(r'\S')
matches(pattern,text_to_search)    

# \b-Word Boundary,\B-Not a Word Boundary,^- Beginning of a String,$- End of a String
pattern=re.compile(r'\bHa')
matches(pattern,text_to_search)    
    
# ^- Beginning of a String,$- End of a String
pattern=re.compile(r'^Start')
matches(pattern,text_to_search)    

pattern=re.compile(r'^a')
matches(pattern,text_to_search)    

pattern=re.compile(r'end$')
matches(pattern,text_to_search)    


# search for phone number with specific format
pattern=re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

with open('data.txt','r',encoding='utf-8') as f:
    contents=f.read()
    matches(pattern,contents)

# search for phone number starting with 800 or 900
pattern=re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches(pattern,text_to_search)    

#specify range to search "-" specifies range
# outside bracket ^ is used to specify starting of string inside bracked to negate the regex
pattern=re.compile(r'[a-zA-z]')
matches(pattern,text_to_search)

pattern=re.compile(r'[1-3]')
matches(pattern,text_to_search)
pattern=re.compile(r'[^a-zA-Z]')
matches(pattern,text_to_search)

pattern=re.compile(r'[^b]at')
matches(pattern,text_to_search)

# Quantifiers: * 0 or More, + 1 or More, ? 0 or One,{3} Exact Number,{3,4}Range of Numbers (Min Max)
pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
matches(pattern,text_to_search)    

# period is optional to match so, ?
pattern=re.compile(r'Mr\.?')
matches(pattern,text_to_search)    

pattern=re.compile(r'Mr\.?\s[A-Z]')
matches(pattern,text_to_search)    

pattern=re.compile(r'Mr\.?\s[A-Z]\w*')
matches(pattern,text_to_search)    

# match groups of patterns
pattern=re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches(pattern,text_to_search)    

# writing regex for emails
pattern=re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches(pattern,emails)    

# Capture information from the groups
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

#group 0 everything else , 1 is domain name, 2 is .com or .gov
def matches_url(pattern,text):
    matches=pattern.finditer(text)
    for match in matches:
        print(match.group(2))

pattern=re.compile(r'https?://?(www\.)?(\w+\.\w+)')
matches_url(pattern,urls)    

domains=pattern.sub(r'\2',urls)
print(domains)

# ingore uppercase or lowercase
pattern=re.compile(r'start',re.IGNORECASE)
matches(pattern,sentence)

# date pattern
dates='''
2020/03/03
2020/12/11
2020/02/01
2020/08/18
'''
pattern=re.compile(r'2020[/][0-1][0-9][/][0-3][0-9]')
matches=pattern.finditer(dates)
for match in matches:
    print(match)
