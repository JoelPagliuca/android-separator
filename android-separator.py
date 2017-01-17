"""
android-separator

gives you all the juicy bits of an apk
puts them in an output folder next to the app
"""
import os
import sys
import zipfile

__all__ = []


APP_NAME = ""   # name of the app
APP_PATH = ""   # path to the app


def usage():
    print "android-separator.py <app.apk>"


def unzip():
    pass


def get_jar():
    pass


def get_source():
    pass


def get_manifest():
    pass


if __name__ == '__main__':
    # check args
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    # go to the app

    # do the things
    unzip()
    get_jar()
    get_source()
    get_manifest()

    sys.exit(0)