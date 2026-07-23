#Code that uses a 'Jar' class to simulate a cookie jar
class Jar:
    def __init__(self, capacity = 12): 
        ...

    def __str__(self):
        ...

    def deposit(self, n): #Add cookies to jar
        ...

    def withdraw(self, n): #Remove cookies from jar
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
