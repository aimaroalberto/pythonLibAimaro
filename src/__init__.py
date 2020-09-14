from builtins import print
import os
import pathlib
from BuildUIFromJson import BuildUIFromJson
from graphicPackage import GraphicPackageManager

#For the directory of the script being run:
path1 = os.path.dirname(os.path.abspath(__file__))
#If you mean the current working directory:
path2 = os.path.abspath(os.getcwd())

path3= pathlib.Path().absolute()
path4= pathlib.Path().absolute().parent
print(path4)

print(path3)
print(path1)
print(path2)

variabile = 0

if variabile:
    #controlBuilds()
    instanzaGrafica = GraphicPackageManager.getInstance()
    instanzaGrafica.showUI()
    #program = Program()
else:
    grafica= BuildUIFromJson()
    grafica.showUI()

print(2 / 28 if variabile == 0 else 5)  #--> beh molto potente!
