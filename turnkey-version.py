#!/usr/bin/python
# Ad-hoc version detection for a system installed from a TurnKey
# appliance. This is a transitory package so we can identify the versions
# in current appliance which were designed before we needed this for
# tklbam. In the future it shouldn't be needed as all appliances will be
# marked with their versions.

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

def _detect_version_packages():
    core = None
    noncore = None

    for fpath in glob.glob("/usr/share/doc/turnkey-*"):
        pkgname = basename(fpath)
        if pkgname in ('turnkey-pylib', 'turnkey-keyring', 'turnkey-release'):
            continue

        m = re.match(r'turnkey-(.*?)-([\d\.]+|beta)', pkgname)
        if not m:
            continue

        codename, release = m.groups()
        dist = parse_changelog(join(fpath, "changelog"))[2]

        if dist == 'turnkey':
            dist = 'lenny'

        version = "turnkey-%s-%s-%s-x86" % (codename, release, dist)
        if codename == 'core':
            core = version
        else:
            noncore = version

    return core, noncore

def get_turnkey_version():
    try:
        return file("/etc/turnkey_version").read().strip()
    except IOError:
        pass

    core, noncore = _detect_version_packages()
    if noncore:
        return noncore
    elif core:
        return core

    raise Error("can't detect turnkey version")
    
def main():
    try:
        print get_turnkey_version()
    except Error, e:
        fatal(e)
    
if __name__=="__main__":
    main()

