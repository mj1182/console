#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
FileTranscriber

A small utility that simulates user typing to aid plaintext file transcription
in limited environments

Usage:

Options:
  -v --version          show program's version number and exit
  -h --help             show this help message and exit
  -i --interval=<time>  Interval between keystrokes (in seconds). Typing too
                        quickly may break applications processing the
                        keystrokes. [default: 0.1]
  -p --pause=<time>     How long the script should wait before starting (in
                        seconds). Increase this if you need more time to enter
                        the typing field. [default: 5]
"""

#This script copied from https://github.com/SavinaRoja/FileTranscriber
#Check there for updates

from docopt import docopt
from pykeyboard import PyKeyboard
from pymouse import PyMouseEvent
import time
import sys

import pygame




#Hack to make input work for both Python 2 and Python 3
try:
    input = raw_input
except NameError:
    pass



def main():
    #Get an instance of PyKeyboard, and our custom PyMouseEvent
    keyboard = PyKeyboard()
    pygame.init()

    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    print("joysticks: ")
    print(joysticks)



    pygame.joystick.quit()
    pygame.quit()




    """
    with open(opts['<file>'], 'r') as readfile:
        for line in readfile:
            keyboard.type_string(line, opts['--interval'])
    """
if __name__ == '__main__':
    opts = docopt(__doc__, version='0.2.1')
    try:
        opts['--interval'] = float(opts['--interval'])
    except ValueError:
        print('The value of --interval must be a number')
        sys.exit(1)
    try:
        opts['--pause'] = float(opts['--pause'])
    except ValueError:
        print('The value of --pause must be a number')
        sys.exit(1)
    main()