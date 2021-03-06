#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Robtex Python.

Usage:
    robtex_python --ip=<ip>
    robtex_python --as=<asn>
    robtex_python --pdns-forward=<hostname>
    robtex_python --pdns-reverse=<ip>
    robtex_python (-h | --help)
    robtex_python --version

Options:
    -h --help     Show this screen.
    --version     Show version.
    --ip=<ip>  IP Address.
    --as=<asn>  ASN.
    --pdns-forward=<hostname>  pDNS Forward Hostname.
    --pdns-reverse=<ip>  pDNS Reverse IP Address.
"""

from docopt import docopt

from .__init__ import __version__ as VERSION
from .robtex_python import ip_query, as_query, pdns_forward, pdns_reverse


def main(arguments=None):
    """Console script for robtex_python"""
    if arguments is None:
        arguments = docopt(__doc__, version=VERSION)
    else:
        # if there are values passed into this function for testing, move along
        pass

    if arguments.get('--ip'):
        return ip_query(arguments['--ip'])
    elif arguments.get('--as'):
        return as_query(arguments['--as'])
    elif arguments.get('--pdns-forward'):
        return pdns_forward(arguments['--pdns-forward'])
    elif arguments.get('--pdns-reverse'):
        return pdns_reverse(arguments['--pdns-reverse'])


if __name__ == "__main__":
    main()
