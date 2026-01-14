# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class

class EmployeeData():
    def __init__(abc,name,department):
        abc.name = name
        abc.department = department


emp1 = EmployeeData("Ankit","Sales")
print(emp1.name,emp1.department)