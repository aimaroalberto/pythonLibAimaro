class Singleton:
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
        self.__listaInutile = list(["partiamo","se", "necessario", "alle", 14])
        self.listaUtile = list([3,2,4,3])
        self.var1=3
        self.__var2=4

    def getVar2(self):
        return self.__var2

    def printBanana(self):
       print("banana")
       for a in self.listaUtile:
           print(a)
       return  5

    def performListExample(self):
        # PythonForProgrammers/list.py
        list = [1, 3, 5, 7, 9, 11]
        print(list)
        list.append(13)
        for x in list:
            print(x)

       # PythonForProgrammers/myFunction.py

    def myFunction(response):
        val = 0
        if response == "yes":
            print("affirmative")
            val = 1
        print("continuing...")
        return val

    def sum(arg1, arg2):
        return arg1 + arg2

# However, if this file is imported as a module into another program, the __main__ code is not executed.