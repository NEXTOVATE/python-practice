#WAP to find factorial of given number using for loop.
n = int(input("Enter a number :"))
fac = 1
for i in range(1,n+1):
           fac = fac*i
print(f"factorial of {n} is {fac}")
 