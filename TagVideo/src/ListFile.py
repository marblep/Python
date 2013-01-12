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

def listVideoFiles(dirname, types):
    allVideos = []
    try:
        for(dirname,dirsub,files) in os.walk(dirname):
            for filename in files:
                lowerfilename = filename.lower()
                for onetype in types:
                    if lowerfilename.endswith('.'+onetype):
                        abspath = os.path.join(os.sep,dirname,filename)
                        info = VideoInfo(abspath,filename, \
                                         os.path.getsize(abspath)/1024/1024, \
                                         os.path.getmtime(abspath))
                        allVideos.append(info)
                        break
    except Exception,e:
        print e

    return allVideos

def getVideoInfo(num):
    outVideos = []
    types = videoTypes
    dirname = videoRootPath
    for(dirname,dirsub,files) in os.walk(dirname):
        for filename in files:
            #print type(filename)
            lowerfilename = filename.lower()
            for onetype in types:
                if lowerfilename.endswith('.'+onetype):
                    abspath = os.path.join(os.sep,dirname,filename)
                    info = VideoInfo(abspath,filename, \
                                     os.path.getsize(abspath)/1024/1024, \
                                     os.path.getmtime(abspath))
                    outVideos.append(info)
                    if(len(outVideos) == num):
                        return outVideos
    return outVideos

def listAllTypes(dirname):
    allTypes = []
    for(dirname,dirsub,files) in os.walk(dirname):
        for filename in files:
            lowerfilename = filename.lower()
            thetype = os.path.splitext(lowerfilename)[1][1:]
            if thetype not in allTypes:
                #abspath = os.path.join()
                allTypes.append(thetype)

    return allTypes

if __name__ == "__main__":
    #'''
    videos = listVideoFiles(videoRootPath, videoTypes)
    print len(videos), " Videos \n"
    sum = 0
    for i in range(len(videos)):
        sum += videos[i].size
    print 'total size: %dG'  %(sum/1024)
    for i in range(len(videos)):
        try:
            print videos[i].abspath.decode('gbk'), "\t", videos[i].size, '\t', videos[i].mtime_str
        except Exception,e:
            print videos[i].abspath.decode('latin-1'), "\t", videos[i].size, '\t', videos[i].mtime_str
    #'''

    
    
