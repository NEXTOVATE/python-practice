class Boy():
    def __init__(self,name,age=17):
        self.name = name
        self.age = age


B1 = Boy("Prince")      #In B1 object the default age of Prince is 17
B2 = Boy("Mayank",16)

print(B1.name,B1.age)
print(B2.name,B2.age) 