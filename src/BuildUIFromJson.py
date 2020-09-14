from tkinter import *
from graphicPackage import  JsonManager

class BuildUIFromJson:
    __instance = None
    _graphicRow = 0
    _items = {}

    def __init__(self):
        self.readedJson = JsonManager.readJson()
        self.window = Tk()
        self.window.title("ReadedJson app app")
        self.window.geometry('500x500')
        lbl = Label(self.window, text="Campi da riempire")
        row=self._assignRow()
        lbl.grid(column=0, row=row)

        actualDictionary = {}
        actualApplication = {}
        for i in self.readedJson.keys():
            self.recursiveBuild(self._items,i,self.readedJson[i],0,False)

            # if isinstance(self.readedJson[i], str):
            #     self.buildInsertPoint(i)
            # if isinstance(self.readedJson[i],list):
            #     Label(self.window, text = i).grid(row= self._assignRow(), column=0)
            #     for j in self.readedJson[i]:
            #         if isinstance(j,dict):
            #             for i in j.keys():
            #                 self.buildInsertPoint(i)
            #         if isinstance(j,str):
            #             self.buildListInsertsPoint(j)

        clickMeBtn = Button(self.window, text="Click Me", command=self.UpdateJson)
        clickMeBtn.grid(column=3, row=0)

    def UpdateJson(self):
        tempJson={}
        for i in self._items.keys():
            self.recoursiveReaderFromGUI(tempJson,i,self._items[i],0,False)

        JsonManager.printJson(tempJson)
        #self.printAllPoint()
        #self.readedJson.

    def showUI(self):
        self.window.mainloop()

    ####define the function that the signup button will do
    def getvalue(self):
        print(self.mystringFromEntryBox.get())
    # *************************************
    def closeUI(self):
        self.window.destroy()

    def createButtonCallack(self):
        self.buildInsertPoint("new coso")

    def printAllPoint(self):
        actualDictionary={}
        actualApplication = {}
        for i in self._items.keys():
            if isinstance(self._items[i], StringVar):
                print(self._items[i])
                actualDictionary[i]=self._items[i].get()
            else:
                for j in self._items[i].keys():
                    actualApplication[j]=self._items[i][j].get()
                actualDictionary[i]=actualApplication
        JsonManager.printJson(actualDictionary)


    def _assignRow(self):
        self._graphicRow += 1
        return self._graphicRow - 1

    def buildInsertPoint(self,itemName):
        row=self._assignRow()
        self._items[itemName]=StringVar()
        self._items[itemName].set(self.readedJson[itemName])
        Label(self.window, text=itemName).grid(row=row , column=0)
        Entry(self.window, textvariable=self._items[itemName]).grid(row=row , column=1)

    def buildListInsertsPoint(self,itemName):
        row=self._assignRow()
        self._items[itemName]=StringVar()
        self._items[itemName].set(itemName)
        Entry(self.window,textvariable=self._items[itemName]).grid(row=row , column=1)

    def buildApplicationInsertPoint(self,itemName):
        row=self._assignRow()
        self._application1[itemName]=StringVar()
        self._application1[itemName].set(itemName)
        #Label(self.window, text=itemName).grid(row=row , column=0)
        Entry(self.window, textvariable=self._application1[itemName]).grid(row=row , column=1)


    def printSelectedButton(self):
        print(print(self.main.get()))

    level=1
    def recursiveBuild(self,objectToBuild, param, paramValue, listParam, isList):
        if isinstance(paramValue,list):
            objectToBuild[param]=[]
            Label(self.window, text=param).grid(row=self._assignRow(), column=0)
            i=0
            for j in paramValue:
                self.recursiveBuild(objectToBuild,param, j, i, True)
                i+=1
        elif isinstance(paramValue,dict):
            Label(self.window, text=param).grid(row=self._assignRow(), column=0)
            objectToBuild[param]={}
            self.level += 1
            for i in paramValue.keys():
                self.recursiveBuild(objectToBuild[param],i, paramValue[i], 0, False)

        elif not(isList):
            objectToBuild[param]=StringVar()
            objectToBuild[param].set(paramValue)
            row=self._assignRow()
            Label(self.window, text=param).grid(row=row, column=0)
            Entry(self.window, textvariable=objectToBuild[param]).grid(row=row, column = self.level)

        elif isList:
            if listParam is 0:
                self._items[param]=[]
            self._items[param].append(StringVar())
            self._items[param][listParam].set(paramValue)
            row=self._assignRow()
            #Label(self.window, text=param).grid(row=row, column=0)
            Entry(self.window, textvariable=self._items[param][listParam]).grid(row=row, column = self.level)




    def recoursiveReaderFromGUI(self, jsonToBuild, param, paramValue, listParam, isList):
        if isinstance(paramValue,list):
            jsonToBuild[param]=[]
            i=0
            for j in paramValue:
                self.recoursiveReaderFromGUI(param, j, i, True)
                i+=1
        elif isinstance(paramValue,dict):
            jsonToBuild[param] = {}
            for i in paramValue.keys():
                self.recoursiveReaderFromGUI(jsonToBuild[param],i, self._items[param][i], 0, False)
        elif not(isList):
            jsonToBuild[param]=self._items[param].get()
        elif isList:
            if listParam is 0:
                jsonToBuild[param]=[]
            jsonToBuild[param].append(self._items[param].get())
            print(self._items[param][listParam].get())