#!/usr/bin/env python3

from distutils.core import setup

setup(
    name="turnkey-version",
    version="1.1",
    author="Jeremy Davis",
    author_email="jeremy@turnkeylinux.org",
    url="https://github.com/turnkeylinux/turnkey-version",
    packages=["sysversion"],
    scripts=["turnkey-version"]
)
