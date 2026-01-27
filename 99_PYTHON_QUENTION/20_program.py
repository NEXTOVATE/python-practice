#WAP to print patterns
a = int(input("Enter your name :"))

for i in range(1,a+1):  
    print("*"*i)                            

b = int(input("Enter your name :"))

for i in range(1,b+1):  
    print(" "*(b-i),"*"*(2*i-1))



c = int(input("Enter your name :"))

for i in range(1,c+1):  
    if i == 1 or i == c:
        print("*"*c)
    else:
        print("*"+" "*(c-2)+"*")