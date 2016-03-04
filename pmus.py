#!/usr/bin/python


import aubio.slicing
from os import listdir
from os.path import isfile, join
import os 
import random

# sudo mount -t vboxsf music /mnt/music

def main():
    """
    main function of the program.

    """
    folderpath = "/mnt/music"

    musics = []
    for dirpath, subdirs, files in os.walk(folderpath):
        for x in files:
            if x.endswith(".mp3"):
                musics.append(os.path.join(dirpath, x))
    #print str(shpfiles)
    print len(musics)
    print random.choice(musics)

if __name__ == '__main__':
    main()
