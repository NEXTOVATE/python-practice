#Write a python OOP program for a studetn management system :
#Create :
#   studetn class(name,roll,mark list)
#   School class that can 
#   add student
#   remove student by roll number
#   search student by partial name
#   Compute average markss of a student

class Stufent:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)
    