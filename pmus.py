#!/usr/bin/python

import aubio
from os import listdir
from os.path import isfile, join
import os 


def main():
    """
    main function of the program.

    """
    folderpath = "/mnt/music"

    shpfiles = []
    for dirpath, subdirs, files in os.walk(folderpath):
        for x in files:
            if x.endswith(".mp3"):
                shpfiles.append(os.path.join(dirpath, x))
    print str(shpfiles)

if __name__ == '__main__':
    main()
