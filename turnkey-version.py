#!/usr/bin/python
import os
from os.path import *

import re
import sys
import glob

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

def parse_changelog(fpath):
    firstline = file(fpath).readline()
    m = re.match(r'(\S+) \((.*?)\) (\w+);', firstline)
    if not m:
        raise Error("couldn't parse changelog '%s'" % fpath)
    
    name, version, dist = m.groups()
    return name, version, dist

def get_turnkey_version():
    try:
        return file("/etc/turnkey_version").read().strip()
    except IOError:
        pass

    for fpath in glob.glob("/usr/share/doc/turnkey-*"):
        pkgname = basename(fpath)
        if pkgname in ('turnkey-pylib', 'turnkey-keyring', 'turnkey-version'):
            continue

        m = re.match(r'(turnkey-.*?)-([\d\.]+|beta)', pkgname)
        if not m:
            continue
        codename, version = m.groups()
        dist = parse_changelog(join(fpath, "changelog"))[2]

        if dist == 'turnkey':
            dist = 'lenny'

        return "%s-%s-%s-x86" % (codename, version, dist)

    raise Error("can't detect turnkey version")
    
def main():
    try:
        print get_turnkey_version()
    except Error, e:
        fatal(e)
    
if __name__=="__main__":
    main()

