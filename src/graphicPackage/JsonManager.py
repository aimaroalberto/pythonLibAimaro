import json

#a need to be a dictionary
def printJson(a):
    out = open("C:/Users/Sistemitaly Srl/Documents/pythonLibAimaro/test/jsonOutput.json",'w')
    out.write(json.dumps(a))
    out.close()

def readJson():
    filein = open("C:/Users/Sistemitaly Srl/Documents/pythonLibAimaro/test/jsonInputExample.json",'r')
    loadedJson = json.load(filein)
    filein.close()
    return loadedJson
