#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# simple path print, delimted line by line entry
# written by george craig, 2016
# this source code is in the public domain
#

# /usr/bin/env python3

import os

path = os.environ['PATH']
path = path.split(";")
for p in path:
    print(p)
