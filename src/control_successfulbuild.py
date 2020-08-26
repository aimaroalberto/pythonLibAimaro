#!/usr/bin/python
import sys

appid=sys.argv[1];

for line in open("log_mvn"+".log"):
  if 'BUILD SUCCESS' in line:
    out = open("/home/sdk/rilascio/buildResults.log", 'a+')
    out.write(appid+': BUILD SUCCESS'+'\n');
    out.close();
    exit();
out = open("/home/sdk/rilascio/buildResults.log", 'a+')
out.write(appid+': BUILD NOT SUCCESS'+ '\n');
out.close();

