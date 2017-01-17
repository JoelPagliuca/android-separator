"""
android-separator

gives you all the juicy bits of an apk
puts them in an output folder next to the app
"""
import os
import sys
import zipfile

__all__ = []

APP_PATH = None   # full path of app
APP_DIR  = None   # path to the app
APP_NAME = None   # name of the app

DEBUG = True


def dprint(msg, tag="DEBUG"):
    if DEBUG:
        print "[{}] {}".format(tag, msg)


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
    dprint("starting")
    # check args
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    dprint("checked args")

    # check if file exists
    APP_PATH = sys.argv[1]
    if not (os.path.exists(APP_PATH) and os.path.isfile(APP_PATH)):
        print APP_PATH + " was not a valid file"
        sys.exit(1)

    APP_NAME = os.path.basename(APP_PATH)
    APP_DIR = os.path.dirname(APP_PATH)
    dprint("working with "+APP_NAME)

    # go to the app
    if APP_DIR:
        dprint("going to directory "+APP_DIR)
        os.chdir(APP_DIR)
        dprint("in directory "+os.getcwd())

    # do the things
    unzip()
    get_jar()
    get_source()
    get_manifest()

    sys.exit(0)