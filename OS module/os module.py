# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:46:22 2020

@author: aishwary
"""

# change directory and get folder names 
import os
from datetime import datetime
#print(dir(os))
os.getcwd()
os.chdir('G:/My Drive/2020/Coding/OS module')
os.listdir()

# create and delete directories
os.mkdir('Random Folder')
os.makedirs('Random Folder/random')
os.rmdir('Random Folder/random')

# rename file
os.rename('test2.xlsx','test.xlsx') 
print(os.stat('test.xlsx'))
mod_time=os.stat('test.xlsx').st_mtime
print(datetime.fromtimestamp(mod_time))

# os walk goes to path and checks all folders and files and returns path,directory and file tuple
for dirpath,dirnames,filenames in os.walk('G:/My Drive/2020/Coding/OS module'):
    print('current path :',dirpath)
    print('directories :',dirnames)
    print('files :',filenames)
    
# Access home directory by getting home enviroment variable
print(os.environ.get('HOME'))
file_path=os.path.join(os.environ.get('HOME'),'test.xslx')
print(file_path)

# os.path
print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))

# check if a file or directory exists
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('G:/My Drive/2020/Coding/OS module'))
print(os.path.isfile('test.xlsx'))


