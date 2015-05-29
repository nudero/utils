#!/usr/bin/python
# -*- coding: utf-8 -*-
# utf8bom_to_utf8.py
# convert utf-8 with bom to utf-8 without bom


import sys
import os, os.path
import shutil
import fileinput
import chardet
from optparse import OptionParser

# -------------- main --------------
if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print "need file path"
	else:
		fp = open(sys.argv[1])
		content  = fp.read()
		detector = chardet.detect(content)
		u = content.decode(detector['encoding'])
		print u

