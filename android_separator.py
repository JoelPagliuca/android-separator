#!/usr/bin/env python
"""
android-separator

gives you all the juicy bits of an apk
puts them in an output folder next to the app

WARNING this runs os.system a few times so if you use an apk with a weird name
and get weird system issues it's your own fault
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
    :rtype: str
    """
    zip_contents = "contents"
    zip_file = zipfile.ZipFile(app, 'r')
    zip_file.extractall(zip_contents)
    zip_file.close()
    return zip_contents


def get_jar(contents_dir):
    """
    get the package jar from the classes.dex

    :param contents_dir: where to find the app contents
    :type contents_dir: str
    :return: location of the classes jar
    :rtype: str
    """
    tag = "GETJAR"
    dprint("get_jar", tag)
    dex_file = os.path.join(contents_dir, "classes.dex")
    if not (os.path.isfile(dex_file)):
        print "classes.dex could not be found"
    dprint(dex_file, tag)
    command = "{dex2jar} {dex_file} -o classes.jar".format(
        dex2jar=os.path.join(TOOL_PATH, D2J),
        dex_file=dex_file
    )
    dprint(command, tag)
    os.system(command)
    dprint("done", tag)


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

    APP_NAME = os.path.basename(APP_PATH)
    APP_DIR = os.path.dirname(APP_PATH)
    dprint("working with "+APP_NAME)

    # go to the app
    if APP_DIR:
        os.chdir(APP_DIR)
        dprint("changed to directory "+os.getcwd())

    # make a new directory to work in
    directory = APP_NAME+"_separated"
    if not os.path.exists(directory):
        os.makedirs(directory)
        dprint("made directory "+directory)
        os.chdir(directory)
        dprint("changed to directory "+os.getcwd())
    else:
        print "output directory already exists, failing"
        sys.exit(1)

    # do the things
    contents_dir = unzip(os.path.join('..', APP_NAME))
    jar_dir = get_jar(contents_dir)
    get_source()
    get_manifest()

    sys.exit(0)