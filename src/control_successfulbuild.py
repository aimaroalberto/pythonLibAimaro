#!/usr/bin/python
import sys

if len(sys.argv) > 1:
  appid=sys.argv[1]

def controlBuilds(filepath):
  for line in open(filepath):
    if 'BUILD SUCCESS' in line:
      out = open("/home/sdk/rilascio/buildResults.log", 'a+')
      out.write(appid+': BUILD SUCCESS'+'\n')
      out.close()
      exit()
  out = open("/home/sdk/rilascio/buildResults.log", 'a+')
  out.write(appid+': BUILD NOT SUCCESS'+ '\n')
  out.close()

