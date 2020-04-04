usage: turnkey-version [-h] |
                       [rootfs] | [-f PATH/TO/FILE] | [-s TKL_VER_STR]
                       [-a] | [-n] [-t] [-c] [-r] | [-j]
                       [-d]

TurnKey Linux Version information

positional arguments:
  rootfs                Path to root filesystem, defaults to '/'. Will read
                        file 'ROOTFS/etc/turnkey_version'.

optional arguments:
  -h, --help            show this help message and exit
  -f PATH/TO/FILE, --file PATH/TO/FILE
                        Absolute or relative path to file containing turnkey
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
  additiona key, value pairs.

  -d, --debian-codename
                        Return system's reported Debian codename. If rootfs
                        set, then return codename of chroot.
