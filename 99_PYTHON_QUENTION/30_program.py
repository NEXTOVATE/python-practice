# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

# Examples(Operator, value1, value2) --> output
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7


def basic_calculation(value1,oper,value2):
    if oper == '+':
        return value1 + value2
    elif oper == '-':
        return value1 - value2
    elif oper == '*':
        return value1 * value2
    elif oper == '/':
        if value2 == 0:
            return "Error : division by zero"
        return value1 / value2
    else:
        return 'Invalid operator'
    


x = int(input("Enter value one :"))
y = input("Enter value opearator :")
z = int(input("Enter value two :"))


print(basic_calculation(x,y,z))


 































