# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:46:59 2020

@author: aishwary
"""

#File objects
from os import chdir
chdir('G:/My Drive/2020/Coding/Input-Output')

# reading 'r', writing 'w', appending 'a', read-write 'r+'
f=open('check.txt','r')
print(f.name)
print(f.mode)
f.close()

# Context manager - use with (closes the file)
with open('check.txt','r') as f:
    f_contents=f.read()
    print(f_contents)
    
with open('check.txt','r') as f:
    f_few_contents=f.readlines()
    print(f_few_contents)

with open('check.txt','r') as f:
    for line in f:
        print(line,end='')

with open('check.txt','r') as f:
    f_contents=f.read(20)
    print(f_contents)

with open('check.txt','r') as f:
    size_to_read=2
    f_contents=f.read(size_to_read)
    while len(f_contents)>0:
        print(f_contents,end='*')
        f_contents=f.read(size_to_read)

# write mode overwrites the existing file, if doesn't exist it creates a new one
with open('test2.txt','w') as f:
    f.write('test')

with open('test2.txt','a') as f:
    f.seek(4)
    f.write('test')

with open('check.txt','r') as rf:
    with open('test2.txt','w') as wf:
        for line in rf:
            wf.write(line)
            
# for pictures add b for binary mode
with open('pic.jpg','rb') as rf:
    with open('copy_pic.jpg','wb') as wf:
        for line in rf:
            wf.write(line)

with open('pic.jpg','rb') as rf:
    with open('copy_pic.jpg','wb') as wf:
        chunk_size=4000
        rf_chunk=rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk=rf.read(chunk_size)

with open('pic.jpg','rb') as rf:
    with open('copy_pic_2.jpg','wb') as wf:
        rf_chunk=rf.read(4000)
        wf.write(rf_chunk)
        