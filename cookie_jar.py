#Code that uses a 'Jar' class to simulate a cookie jar

class Jar: 
    def __init__(self, capacity = 12): 
        self._capacity = capacity #Get our capacity, put in _ to differentiate from normal capacity variable
        if capacity < 0: #If our capacity is negative now, raise ValueError
            raise ValueError
        self._size = 0 #Start with 0 cookies in, _ for please don't touch

    def __str__(self): #Print out a cookie emoji for each cookie in jar
        return "🍪" * self._size #For each cookie in the jar, return a cookie emoji. This assumes everything is good, no error checking

    def deposit(self, n): #Add cookies to jar
        if self._size + n > self._capacity: #If we go over our capacity, raise ValueError
            raise ValueError
        self._size += n #Otherwise, add cookies

    def withdraw(self, n): #Remove cookies from jar
        if (n > self._size) or (n < 0): #If we try to remove more cookies than we have in the jar, or if n is negative, raise ValueError
            raise ValueError
        self._size -= n #Otherwise, remove cookies

    @property
    def capacity(self): #Return capacity
        return self._capacity

    @property
    def size(self): #Return size
        return self._size

