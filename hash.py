#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# simple sha-* hash of file specified
# I.e., hash <type> <filename>
# Ouput: <hash-value>
# written by george craig, 2016
# this source code is in the public domain
#

import sys, hashlib

params = len(sys.argv)
hashtype = ""
filename = ""

if ((params == 2) or (params == 3)):

    if (params == 3):
        hashtype = sys.argv[1]
        filename = sys.argv[2]
    else:
        hashtype = "sha512"
        filename = sys.argv[1]

    BLOCKSIZE = 65536 #64k reads
    hasher = hashlib.new(hashtype) #sha512
    
    #hasher.update
    #hasher.update(b'collection of bytes')
    #print(hashlib.algorithms_available)
    #hasher = hashlib.md5()
    #hasher = hashlib.sha512()
    
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    
    print(hashtype + ": ", hasher.hexdigest())
    #print('block size: ', hasher.block_size)
    #print('digest size: ', hasher.digest_size)

else:
 
    sys.stderr.write("Usage: hash <type> <file>\n")
    sys.stderr.write("hash calculates the hash value of the specified file\n")
    sys.stderr.write("Written by George Craig, 2016. Public domain.\n")
    sys.stderr.write("This program comes with ABSOLUTELY NO WARRANTY; this is free software, and you are welcome to\n")
    sys.stderr.write("Parameters:\n")
    sys.stderr.write("  <type>  md5, sha256, sha512 (default)\n")
    sys.stderr.write("  <file>  location of file to hash i.e., c:\\file.txt, /home/user/file.txt\n")
    sys.stderr.write("\n")
