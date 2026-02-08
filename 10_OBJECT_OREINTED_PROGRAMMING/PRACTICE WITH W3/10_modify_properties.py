# You can modify the value of properties on objects:
# Change the age property:

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

    
P1 = Person("Monu",13)

P1.age = 15             #modify the age 
print(P1.name,P1.age) ``