class StudentData():
    def __init__(self,roll_no,name,age,course,total_fee,):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course
        self.total_fee = total_fee


stu1 = StudentData(121,"Sagar",14,"DIT",15500)

print(stu1.roll_no,stu1.name,stu1.age,stu1.course,stu1.total_fee)