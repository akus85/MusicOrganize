import eyeD3
from os import getcwd, listdir, mkdir, path
from shutil import move
from sys import argv

IN_FILES_PATH = argv[1]
OUT_FILES_PATH = argv[2]

def getFiles():
    return listdir(IN_FILES_PATH)

def checkDir(dir):
    if (path.exists(dir) == False):
        mkdir(dir)

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
    


# --- MAIN ---#
checkDir(OUT_FILES_PATH)
l = getFiles()
for i in l:
    readTag(i)
