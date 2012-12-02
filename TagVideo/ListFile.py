import os

videoTypes = ['wmv','avi','rmvb','rm','mkv','mp4','flv','mpg','3gp']

def listVideoFiles(dirname, types):
    allVideos = []
    for(dirname,dirsub,files) in os.walk(dirname):
        for filename in files:
            lowerfilename = filename.lower()
            for onetype in types:
                if lowerfilename.endswith('.'+onetype):
                    allVideos.append(filename)
    return allVideos
    

def listAllTypes(dirname):
    allTypes = []
    for(dirname,dirsub,files) in os.walk(dirname):
        for filename in files:
            lowerfilename = filename.lower()
            thetype = os.path.splitext(lowerfilename)[1][1:]
            if thetype not in allTypes:
                allTypes.append(thetype)

    return allTypes

#'''
videos = listVideoFiles(r'D:\Marble\bt\FlashGet', videoTypes)
print len(videos)
#for video in videos:
#    print video
#'''
'''
types = listAllTypes(r'D:\Marble\bt\FlashGet')
print len(types)
for item in types:
    print item
'''

'''
for (dirname,subshere,fileshere) in os.walk(r'C:\Intel'):
    print '[{0}]'.format(dirname)
    for fname in fileshere:
        print os.path.join(dirname, fname)
'''

'''
dirname = r'C:'
for file in glob.glob(dirname + '/*.txt'):
    head, tail = os.path.split(file)
    print head, tail, '=>', ('D:\\other\\'  + tail)
'''
