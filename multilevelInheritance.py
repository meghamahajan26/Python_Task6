class Electronics:
    def power_on(self):
        print("Electronics powered on")

class Computer(Electronics):  
    def boot(self):
        print("Computer booting up")

class Laptop(Computer):  
    def fold(self):
        print("Laptop folded")

laptop = Laptop()
laptop.power_on()  
laptop.boot()      
laptop.fold()     
