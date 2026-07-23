#Code that uses a 'Jar' class to simulate a cookie jar

class Jar: 
    def __init__(self, capacity = 12): 
        self._capacity = capacity #Get out capacity
        if capacity != 12: #If our capacity got messed with, 
            raise ValueError
        self._size = 0 #Start with 0 cookies in 

    def __str__(self): #Print out a cookie emoji for each cookie in jar
        return "🍪" * self._size #For each cookie in the jar, return a cookie emoji

    def deposit(self, n): #Add cookies to jar

        self.n = n 


    def withdraw(self, n): #Remove cookies from jar
        self.n = n

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

