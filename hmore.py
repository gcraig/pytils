#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# simple hexadecimal "more"
# written by george craig, 2016
# this source code is in the public domain
#

import random, sys

inf = None
content = 0

if (len(sys.argv) > 1):
    with open(sys.argv[1], 'r') as info:
        content = info.read()

else:
    inf = sys.stdin
    content = inf.read()

ctr = 0
addr = 0
data = len(content) > 0;

# todo: dyn addr size
if (data):
    print "0x00000000 ",

for i in range(0, len(content)):

    print "{0:02x}".format(ord(content[i])),

    ctr = ctr + 1
    if ((ctr == 10) or (i == len(content) - 1 )):

        print " ",

        # todo: scrub this content for
        # CR, LF, and print .
        if (i < 11):
            print content[0:10],
        else:
            # todo: pad, less than 0x10 chars
            print content[i-ctr:i],
        print
        addr = addr + 0x10
        print "0x" + "{0:08x} ".format(addr),
        ctr = 0

