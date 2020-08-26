from singletonExample import Singleton

print("stronzo")

#Singleton.printBanana(Singleton.getInstance())

ciao = list(["3",3,"43",Singleton])
ciao.append("fcia")
print(ciao)
#print(ciao.pop(2))

istanza = Singleton.getInstance()
print(istanza)
print(Singleton.getInstance().var1)
#Singleton.getInstance()._Singleton__var2=5
c = Singleton.getVar2(Singleton.getInstance())
c=5
print(Singleton.getVar2(Singleton.getInstance()))
print(dir(Singleton.getInstance()))