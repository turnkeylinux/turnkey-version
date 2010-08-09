#!/usr/bin/python
import os
from os.path import *
import sys
import getopt

def usage(e=None):
    if e:
        print >> sys.stderr, "error: " + str(e)

    print >> sys.stderr, "Syntax: %s [args]" % sys.argv[0]
    print >> sys.stderr, __doc__.strip()
    sys.exit(1)

class Error(Exception):
    pass

def fatal(s):
    print >> sys.stderr, "error: " + str(s)
    sys.exit(1)

def get_turnkey_version():
    try:
        return file("/etc/turnkey_version").read().strip()
    except IOError:
        pass

    raise Error("can't detect turnkey version")
    
def main():
    try:
        print get_turnkey_version()
    except Error, e:
        fatal(e)
    
if __name__=="__main__":
    main()

