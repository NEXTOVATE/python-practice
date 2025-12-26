#solve the program1 with while loop
#WAP to print multiplication table of a given number using for loop

n = int(input("Enter a number :"))

i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i +=1