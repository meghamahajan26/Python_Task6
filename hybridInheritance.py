class Animal:
    def breathe(self):
        print("Animal breathes")

class Mammal(Animal):  
    def give_birth(self):
        print("Mammal gives birth")

class Bird(Animal):  
    def lay_eggs(self):
        print("Bird lays eggs")

class Bat(Mammal, Bird):  
    def fly(self):
        print("Bat can fly")

bat = Bat()
bat.breathe()     
bat.give_birth()  
bat.lay_eggs()   
bat.fly()         
