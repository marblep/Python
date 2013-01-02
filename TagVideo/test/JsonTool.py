# file <-1-> json string <-2-> python object <-3-> VideoInfo <-4-> UI

#1. read/write file
#2. python json API
#3. merge into ListFile.py

# Pickle

import os

'''
curdir = os.path.abspath('.')
abspath = os.path.join(curdir, 'setting.txt')
print os.path.exists(abspath)

thefile = open('setting.txt', 'w')
thefile.write('hello \n')
thefile.write('python \n')
thefile.close()

'''
'''
import json
from pprint import pprint

with open('setting.txt') as data_file:
    data = json.load(data_file)

print data['maps'][1]['id']
'''
import json

data = [ { 'a':'A', 'b':(2, 4,6,8), 'c':3.0 } ]
print 'DATA:', repr(data)

data_string = json.dumps(data, indent=2)
print 'JSON:', data_string
