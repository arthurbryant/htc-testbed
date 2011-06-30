#!/usr/bin/env python
# This file is used to parse Apache log to get time and query or id. 
# Author: Arthur
# Date: 2011/06/30

import re
import sys
import time

def convert_date_to_seconds(date):
    #date example: 16/Nov/2010:16:12:29
    dt = time.strptime(date, "%d/%b/%Y:%H:%M:%S")
    return time.mktime(dt)

if len(sys.argv) < 3:
    print "Usage: parse_apache_log.py input_logs output"
    sys.exit(-1)
input = sys.argv[1]
output = sys.argv[2]

out = open(output, "w")
if out is None:
    print "Create output file failed"
    sys.exit(-1)

#pid = re.compile("\[(.*) .*\] \".* \/{.*person\/|{department|institute}\.php?id=}(\d+) HTTP")
pid = re.compile("\[(.*) .*\] \".* \/(person\/|(institute|department)\.php\?id=)(\d+)")
pstr = re.compile("\[(.*) .*\] \".* \/search\.php\?query=(.*) HTTP")

with open(input) as f:
    for line in f.readlines():
        res = pid.search(line)
        res2 = pstr.search(line)
        if res:
            date = convert_date_to_seconds(res.group(1))
            out.write(str(date) + " ")
            out.write(res.group(4) + "\n")
        if res2:
            date = convert_date_to_seconds(res2.group(1))
            out.write(str(date) + " ")
            out.write(res2.group(2) + "\n") 
        #else:
        #    print "not found"
f.close()
out.close()
