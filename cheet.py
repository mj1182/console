#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Cheet

A cheet command

Usage:
    cheet <cmd>

Options:
    -h --help       this is the help

"""

from docopt import docopt
import subprocess

def main():
    cmd =  opts['<cmd>']
    output = ''

    if cmd == 'git':
        output = 'git es muy bueno'
    subprocess.call(['echo', output])

if __name__ == '__main__':
    opts = docopt(__doc__)

    main()

