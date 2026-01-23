# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number):
        if number % 2 == 0:
            number *=8
        else:
            number *=9
        return number 





n = int(input("Enter the number :"))

z = simple_multiplication(n)
print(z)

