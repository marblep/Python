# -*- coding: utf8 -*-
import os
import time
import sys

videoRootPath = r'D:\Marble\bt\FlashGet'
videoTypes = ['wmv','avi','rmvb','rm','mkv','mp4','flv','mpg','3gp']

class VideoInfo:
    def __init__(self, abspath_, filename_, size_, mtime_):
        self.abspath = abspath_
        self.filename = filename_
        self.size = size_
        self.mtime = mtime_
        self.mtime_str = time.ctime(mtime_)

def isVideo(filename):
    lowername = filename.lower()
    for type in videoTypes:
        if lowername.endswith('.'+type):
            return True
    return False
        
    
def listVideoFiles(dirname, types):
    allVideos = []
    for(dirname,dirsub,files) in os.walk(dirname):
        for filename in files:
            if isVideo(filename):
                abspath = os.path.join(os.sep,dirname,filename)
                info = VideoInfo(abspath,filename, os.path.getsize(abspath)/1024/1024,  os.path.getmtime(abspath))
                allVideos.append(info)            

    return allVideos

def getVideoInfo(num):
    outVideos = []
    dirname = videoRootPath
    for(dirname,dirsub,files) in os.walk(dirname):
        for filename in files:
            if isVideo(filename):
                abspath = os.path.join(os.sep,dirname,filename)
                info = VideoInfo(abspath,filename, os.path.getsize(abspath)/1024/1024,  os.path.getmtime(abspath))
                outVideos.append(info)
                if len(outVideos) == num :
                    return outVideos
    return outVideos

def listAllTypes(dirname):
    allTypes = []
    for(dirname,dirsub,files) in os.walk(dirname):
        for filename in files:
            lowerfilename = filename.lower()
            thetype = os.path.splitext(lowerfilename)[1][1:]
            if thetype not in allTypes:
                allTypes.append(thetype)

    return allTypes

if __name__ == "__main__":
    #'''
    videos = listVideoFiles(videoRootPath, videoTypes)
    print len(videos), " Videos \n"
    totalsize = 0
    for i in range(len(videos)):
        totalsize += videos[i].size
    print 'total size: %dG'  %(totalsize/1024)
    
    '''
    for i in range(len(videos)):
        try:
            print videos[i].abspath.decode('gbk'), "\t", videos[i].size, '\t', videos[i].mtime_str
        except Exception,e:
            print videos[i].abspath.decode('latin-1'), "\t", videos[i].size, '\t', videos[i].mtime_str
    '''

    
    
