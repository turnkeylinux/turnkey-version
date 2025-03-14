# Copyright (c) 2010 Liraz Siri <liraz@turnkeylinux.org>
# Copyright (c) 2020-2025 TurnKey GNU/Linux <admin@turnkeylinux.org>
#
# This file is part of turnkey-version.
#
# turnkey-version is open source software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.

import re
import subprocess
import os
from typing import Optional

DEFAULT = 'etc/turnkey_version'


class TurnkeyVersionError(Exception):
    pass


def _parse_turnkey_release(version: str) -> str:
    m = re.match(r'turnkey-.*?-(\d.*?)-[^\d]', version)
    if m:
        return m.group(1)
    return ''


def get_debian_codename(rootfs: str = '/') -> str:
    """Return Debian codename of the system (leverages lsb_release)"""
    comm = ['lsb_release', '-sc']
    if rootfs != '/':
        comm = ['chroot', rootfs] + comm
    proc = subprocess.run(comm, capture_output=True, text=True)
    if proc.returncode != 0:
        raise TurnkeyVersionError(f"lsb_release failed: {proc}'")
    return proc.stdout.rstrip()


def get_turnkey_release(rootfs: str = '/') -> Optional[str]:
    """Return release_version. On error, returns None"""
    turnkey_version = get_turnkey_version(rootfs=rootfs)
    if turnkey_version:
        return _parse_turnkey_release(turnkey_version)
    return None


# used by turnkey-version
def get_turnkey_version(rootfs: str = '/',
                        fpath: str = DEFAULT
                        ) -> Optional[str]:
    """Return turnkey_version. On error, returns None.
    Warning: if fpath is an absolute path, rootfs will be ignored.
    """
    try:
        with open(os.path.join(rootfs, fpath), 'r') as fob:
            return fob.read().strip()
    except IOError:
        pass
    return None


class AppVer:
    def __init__(self, turnkey_version: str | None = None, rootfs: str = '/'):
        if not turnkey_version:
            turnkey_version = get_turnkey_version(rootfs=rootfs)
        if not turnkey_version:
            raise TurnkeyVersionError('Error: No TurnKey version found')
        if turnkey_version.startswith('turnkey-'):
            turnkey_version = turnkey_version[8:]
        self.appname, self.tklver, self.codename, self.arch \
                = turnkey_version.rsplit('-', 3)
        self.deb_codename = get_debian_codename(rootfs=rootfs)

    def app_ver(self) -> tuple[str, str, str, str]:
        return (self.appname, self.tklver, self.codename, self.arch)

    def app_json(self, deb_ver: bool = False) -> dict[str, str]:
        _json = {'name': self.appname, 'tklver': self.tklver,
                 'codename': self.codename, 'arch': self.arch}
        if deb_ver:
            _json['debian_codename'] = self.deb_codename
        return _json


# used by turnkey-sysinfo
def fmt_base_distribution() -> str:
    """Return a formatted distribution string:
        e.g., Debian 10/Buster"""
    proc = subprocess.run(["lsb_release", "-ircs"],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise TurnkeyVersionError(f'lsb_release failed: {proc}')
    distro, release, codename = proc.stdout.splitlines()
    return f"{distro} {release}/{codename.capitalize()}"


def fmt_sysversion() -> str:
    version_parts = []
    release = get_turnkey_release()
    if release:
        version_parts.append("TurnKey GNU/Linux {}".format(release))

    basedist = fmt_base_distribution()
    if basedist:
        version_parts.append(basedist)

    if len(version_parts) == 2:
        version = '{} ({})'.format(version_parts[0], version_parts[1])
    elif len(version_parts) == 1:
        version = version_parts[0]
    else:
        version = "Unknown"
    return version
