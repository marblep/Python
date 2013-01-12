# -*- coding: UTF-8 -*-
import shelve
import os

#stars = ('zero', 'one', 'two', 'three', 'four', 'five')

class CreatedTags:
    def __init__(self):
        self.tags = ['欧美','熟女','SM','制服','群交','美女','三级']
        
    def log(self):
        info = 'CreatedTags: '
        for item in self.tags:
            info += (item + ', ')
        print info
        
class TagAndStar:
    def __init__(self, filename):
        self.star = 0
        self.tags = []
        self.key = filename
        
    def log(self):
        info = str(self.star) + ' ' 
        for tag in self.tags:
            info += (tag + ', ')
        print info
       
def CreateDB():
    files = [TagAndStar('aa'), TagAndStar('bb'), TagAndStar('cc')] 
    createdTags = CreatedTags()
    
    db = shelve.open('test_fileinfo_db')
    db['Tags'] = createdTags
    for info in files:
        db[info.key] = info
    
    db.close()
    
def ReadDB():
    db = shelve.open('test_fileinfo_db')
    #print len(db)
    for key in db:
        db[key].log()
    db.close()
        
def ReadSortedDB():
    pass

def WriteDB():
    db = shelve.open('test_fileinfo_db')
    
    '''
    fb = db['bb']
    fb.star = 5
    fb.tags.append('熟女')
    db['bb'] = fb
    '''
    
    newtags = db['Tags']
    delitem = '素人'
    if delitem in newtags.tags:
        newtags.tags.remove(delitem)  
    #newtags.tags.append('素人')
    db['Tags'] = newtags
    
    db.close()
    
#CreateDB()
WriteDB()
ReadDB()


        
'''
dbase = shelve.open("mydbase")
object1 = ['The', 'bright', ('side', 'of'), ['life']]
object2 = {'name': 'Brian', 'age': 33, 'motto': object1}
dbase['brian']  = object2
dbase['knight'] = {'name': 'Knight', 'motto': 'Ni!'}

print len(dbase)
del dbase['brian']
print len(dbase)

dbase.close()


#os.remove('mydbase')
'''
