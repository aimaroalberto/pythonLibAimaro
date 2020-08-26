#!/usr/bin/python
import sys
import shutil

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

version=sys.argv[1];
out = open("new_pom.xml", 'w')
cnt=0;

for line in open("pom.xml"):
  if '<version>' in line and cnt==0:
    nuovo = '	<version>'+version+'</version>\n'
    out.write(nuovo)
    cnt=1;
  else:
    out.write(line)

out.close()

shutil.move("new_pom.xml","pom.xml")