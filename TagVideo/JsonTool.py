# file <-1-> json string <-2-> python object <-3-> VideoInfo <-4-> UI

#1. read/write file
#2. python json API
#3. merge into ListFile.py

import os
 
curdir = os.path.abspath('.')
abspath = os.path.join(curdir, 'setting.txt')
print os.path.exists(abspath)

thefile = open('setting.txt', 'w')
thefile.write('hello \n')
thefile.write('python \n')
thefile.close()

