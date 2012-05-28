#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

__author__ = 'Yuta Hayashibe' 
__version__ = ""
__copyright__ = ""
__license__ = "GPL v3"

DUMMYFILENAME='dummy.txt'
BIN_PATH=u"/usr/local/bin/ssgnc-search"
DIR = u'/data/google-ngram-en/index/'
import corrcha.tool.ssgnc
ssgnc = corrcha.tool.ssgnc.Ssgnc(BIN_PATH, DIR)

def search(query):
    ssgnc.search(query)

def testSpeed():
    i = 0
    from time import time
    start = time()
    line = allLines = open(DUMMYFILENAME).read()
    items = line.split()
    leng = len(items)
    for item in items:
        search(item)
        i += 1
    for j in xrange(0, leng-3):
        search(" ".join(items[j:j+2]))
        search(" ".join(items[j:j+3]))
        i += 2
    end = time()
    return end - start, i


print "======"
print "===SPEED TEST (x3)==="
for i in xrange(0,3):
    tm, cnt = testSpeed()
    print "%dth : %f (%d times call)" % (i, tm, cnt)
print "===FINISED==="
print "======"


#if __name__ == '__main__':
