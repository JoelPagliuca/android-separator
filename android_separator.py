"""
android-separator

gives you all the juicy bits of an apk
puts them in an output folder next to the app
"""
import os
import sys
import zipfile

__all__ = []


TOOL_PATH = None  # path for where apktool, cfr, d2j are
CFR = "cfr_0_119.jar"
APKTOOL = "apktool"
D2J = "d2j-dex2jar.sh"

APP_PATH = None   # full path of app
APP_DIR = None    # path to the app
APP_NAME = None   # name of the app

DEBUG = True


def dprint(msg, tag="DEBUG"):
    """
    print a debug message
    :param msg: message to be printed
    :type msg: str
    :param tag: [tag] will be printed before msg
    :type tag: str
    :return: None
    """
    if DEBUG:
        print "[{}] {}".format(tag, msg)


def usage():
    """
    print usage
    :return: None
    """
    print "android_separator.py <app.apk>"


def unzip(app):
    """
    unzip the app and put the contents in a new folder
    :param app: name of the app
    :type app: str
    :return: name of directory with unzip contents
    """
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

    TOOL_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tools")
    dprint("tools are in "+TOOL_PATH)

    # check if file exists
    APP_PATH = sys.argv[1]
    if not (os.path.exists(APP_PATH) and os.path.isfile(APP_PATH)):
        print APP_PATH + " was not a valid file"
        sys.exit(1)


    # make a new directory to work in

    APP_NAME = os.path.basename(APP_PATH)
    APP_DIR = os.path.dirname(APP_PATH)
    dprint("working with "+APP_NAME)

    # go to the app
    if APP_DIR:
        os.chdir(APP_DIR)
        dprint("changed to directory "+os.getcwd())

    # do the things
    unzip(APP_NAME)
    get_jar()
    get_source()
    get_manifest()

    sys.exit(0)