usage: turnkey-version [-h] [-f PATH_TO_FILE] [-s TKL_VER_STR] [-n] [-t] [-c]
                       [-r] [-a] [-j] [-d]
                       [rootfs]

TurnKey Linux Version information

positional arguments:
  rootfs                Path to root filesystem, defaults to '/'. Will read
                        file 'ROOTFS/etc/turnkey_version'.

optional arguments:
  -h, --help            show this help message and exit
  -f PATH_TO_FILE, --file PATH_TO_FILE
                        Absolute (i.e. leading /) or relative (to current;
                        i.e. no leading /) path to file containing turnkey
                        version string. NOTE: conflicts with -s|--string.
  -s TKL_VER_STR, --string TKL_VER_STR
                        Process a string, instead of reading from a
                        file.('turnkey-' prefix optional). NOTE: Conflicts
                        with -f|--file.

Output options:
  Return space separated values, or all values in json format. NOTE: If
  multiple elements returned, the order will always be: 'NAME VERSION
  CODENAME ARCH' (regardless of switch order).

  -n, --name            Return TurnKey appliance name. E.g. core.
  -t, --tklversion      Return TurnKey version number. E.g. 16.0.
  -c, --codename        Return relevant Debian codename. E.g. buster.
  -r, --arch            Return relevant architechture. E.g. amd64
  -a, --all             Return space separated name, version, codename & arch.
                        (Same as -ntcr).
  -j, --json            Return all name info in json format (conflicts with
                        other output options).

Additional output options:
  Return additional values. If no other output options specified, these will
  be the only output. Otherwise, these values will be appended after any
  other results returned, either space separated, or if -j|--json, as
  additional key, value pairs.

  -d, --debian-codename
                        Return system's reported Debian codename (not TurnKey
                        version codename). If rootfs set, then return codename
                        of chroot.
