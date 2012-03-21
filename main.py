import eyeD3
from os import listdir, mkdir, path
from shutil import move
from sys import argv

#IN_FILES_PATH = argv[1]
#OUT_FILES_PATH = argv[2]

IN_FILES_PATH = ""
OUT_FILES_PATH = ""
PLAYLIST_PATH = ""

def getFiles(path):
    return listdir(path)

def checkDir(path):
    if (path.exists(path) == False):
        mkdir(path)

def makeDir1(namedir):
    try:
        mkdir(OUT_FILES_PATH + namedir.replace(' ', '_'))
    except: pass

def makeDir2(namedir1, namedir2):
    try:
        mkdir(OUT_FILES_PATH + namedir1.replace(' ','_') + '/' + namedir2.replace(' ', '_'))
    except: pass

def moveFile(srcFile, destFile):
    move(srcFile, destFile)
    
def readTag(mfile):
    mfile = unicode(mfile,'utf-8')
    tag = eyeD3.Tag()
    tag.link(IN_FILES_PATH + mfile)
    makeDir1(tag.getArtist())
    makeDir2(tag.getArtist(), tag.getAlbum())
    src = IN_FILES_PATH + mfile
    dest = OUT_FILES_PATH + tag.getArtist().replace(' ','_') + '/' + tag.getAlbum().replace(' ','_') + '/' + mfile
    moveFile(src,dest)
    
def makePlaylist():
    songs = getFiles(PLAYLIST_PATH)
    f = open(PLAYLIST_PATH + "playlist.m3u", "w")
    for song in songs:
        if (song[-4:] == '.mp3'):
            f.writelines(PLAYLIST_PATH + song + '\n')
    f.close()
        
    
def parseMenu():
    global IN_FILES_PATH, OUT_FILES_PATH, PLAYLIST_PATH
    if ((argv[1] == '-o')or(argv[1] == '-organize')):
        IN_FILES_PATH = argv[2]
        OUT_FILES_PATH = argv[3]
        checkDir(OUT_FILES_PATH)
        l = getFiles(IN_FILES_PATH)
        for i in l:
            readTag(i)
    elif ((argv[1] == '-p')or(argv[1] == '-playlist')):
        PLAYLIST_PATH = argv[2]
        makePlaylist()

# --- MAIN ---#
parseMenu()