class Protected: ### Here I am defining the protected clas
    def __init__(self):
        self._protectedVar = 0 ## here i am assinging the protected var to 0
    def getPrivate(self):
          print(self._protectedVar)
    
    def setPrivate(self, private):
        self._protectedVar = private


    
class Private: ## here I am defing the private class
    def __init__(self):
        self.__privateVar = 12 ## setting private var to 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private





obj = Protected() # creation of object for protected 
obj._protectedVar = 34
obj1 = Private()# creation of obj for private 
obj1.getPrivate() 
obj1.setPrivate(23)
obj1.getPrivate()
print(obj._protectedVar)
