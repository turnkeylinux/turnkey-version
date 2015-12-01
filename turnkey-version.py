#!/usr/bin/python
# Ad-hoc version detection for a system installed from a TurnKey
# appliance. This is a transitory package so we can identify the versions
# in current appliance which were designed before we needed this for
# tklbam. In the future it shouldn't be needed as all appliances will be
# marked with their versions.

from os.path import join

import sys

def usage(e=None):
    if e:
        print >> sys.stderr, "error: " + str(e)

    print >> sys.stderr, "Syntax: %s [rootfs]" % sys.argv[0]
    sys.exit(1)

class Error(Exception):
    pass

def fatal(s):
    print >> sys.stderr, "error: " + str(s)
    sys.exit(1)

def get_turnkey_version(rootfs):
    try:
        return file(join(rootfs, "etc/turnkey_version")).read().strip()
    except IOError:
	    raise Error("can't detect turnkey version - missing /etc/turnkey_version file")

def main():
    args = sys.argv[1:]

    rootfs = "/"
    if args:
        if args[0] in ('-h', '--help'):
            usage()

        if len(args) != 1:
            usage("incorrect number of arguments")

        rootfs = args[0]

    try:
        print get_turnkey_version(rootfs)
    except Error, e:
        fatal(e)

if __name__=="__main__":
    main()

