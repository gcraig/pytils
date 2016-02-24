#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, random

#
# simple password random creator
# createpwd 10 = 10 character password
# written by george craig, 2016
# this source code is in the public domain
#

length = 10
newpwd = ""
tokens = "@#$%^&*_/?!ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

if (len(sys.argv) > 1):
    length = int(sys.argv[1])

for i in range(length):
    idx = random.randrange(len(tokens))
    newpwd = newpwd + tokens[idx]

print newpwd
