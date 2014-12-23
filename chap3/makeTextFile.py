'''
Created on Dec 23, 2014

@author: seashell
'''
#! /usr/env/env python
'makeTextFile.py  -- create text file'

import os

# get file name
while True:
    fname = raw_input('Enter file name: ')
    if os.path.exists(fname):
        print 'error, file already exists!'
    else:
        break

# get file content
all = []
print "\nEnter lines ('. by itself will quit')\n"
while True:
    entry = raw_input('>>>')
    if entry == '.':
        break;
    else:
        all.append(entry)
        
#write lines to file
fobj = open(fname, 'w')
fobj.write('\n'.join(all))
fobj.close()
print 'Done!'
    
        