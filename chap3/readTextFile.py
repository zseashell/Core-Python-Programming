'''
Created on Dec 23, 2014

@author: seashell
'''
#! /usr/env/env python
'readTextFile.py  -- read text file and display it'

# get file name
fname = raw_input('Enter filename: ')
print

# try to open file for reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print "***file doesn't exist!"
else:
    # display content
    for eachline in fobj:
        print eachline
    fobj.close()
    
