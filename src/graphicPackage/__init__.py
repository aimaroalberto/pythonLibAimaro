from tkinter import *
from graphicPackage import  JsonManager
BEGIN_OF_ARRAY="1.0"
DELETE_FINAL_LINEFEED="-1c"
#from varname import nameof

class GraphicPackageManager:
    __instance = None
    _graphicRow = 0
    _items = {}
    @staticmethod
    def getInstance():
        """ Static access method. """
        if GraphicPackageManager.__instance == None:
            GraphicPackageManager()
        return GraphicPackageManager.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if GraphicPackageManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            GraphicPackageManager.__instance = self
            self.window = Tk()
            self.window.title("Welcome to Alberto app")
            self.window.geometry('350x350')
            lbl = Label(self.window, text="Campi da riempire")
            row=self._assignRow()
            lbl.grid(column=0, row=row)

            #self.hi_there.pack(side="top")  --> se uso grid non posso usare pack
            #self.mystringFromEntryBox=StringVar()
            #Entry(self.window, textvariable=self.mystringFromEntryBox).grid(row=self._assignRow(), column=0, sticky=E)  # entry textbox
            #sticky parameter: North/Sud/Ovest/Est

            self.buildInsertPoint("main")
            self.buildInsertPoint("maii2n")

            Button(self.window, text="create", command=self.createButtonCallack).grid(row=self._assignRow(), column = 0)

            row=self._assignRow()
            clickMeBtn = Button(self.window, text="Click Me", command=self.printAllPoint)
            clickMeBtn.grid(column=0, row=row)
            self.quit = Button(self.window, text="QUIT", fg="red",
                               command=self.closeUI)
            self.quit.grid(column=1, row=row)

            #----------------------------------------------------------------------------
            lblStartOfApplication = Label(self.window, text="Inserisci applicazione")
            lblStartOfApplication.grid(row=self._assignRow(),column=0)
            self._application1={}
            self._items["grantlist"]=self._application1
            self.buildApplicationInsertPoint("fileName")
            self.buildApplicationInsertPoint("appIdentifier")

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
        Label(self.window, text=itemName).grid(row=row , column=0)
        Entry(self.window,textvariable=self._items[itemName]).grid(row=row , column=1)

    def buildInsertsPoint(self,itemName,itemValue):
        row=self._assignRow()
        self._items[itemName]=StringVar()
        self._items[itemName]=itemValue
        Label(self.window, text=itemName).grid(row=row , column=0)
        Entry(self.window,textvariable=self._items[itemName]).grid(row=row , column=1)

    def buildApplicationInsertPoint(self,itemName):
        row=self._assignRow()
        self._application1[itemName]=StringVar()
        Label(self.window, text=itemName).grid(row=row , column=0)
        Entry(self.window, textvariable=self._application1[itemName]).grid(row=row , column=1)

    def printSelectedButton(self):
        print(print(self.main.get()))
















    def buildAnotherVersionOfTestInsertion(self):
        row = self._assignRow()
        self.T = Text(self.window, height=10, width=30)
        self.T.grid(column=0, row=row)
        self.btn = Button(self.window, text="Click Me", command=self.printTextContent)
        self.btn.grid(column=0, row=row)

    def printTextContent(self):
        print(self.T.get(BEGIN_OF_ARRAY,END+DELETE_FINAL_LINEFEED))
        self.getvalue()