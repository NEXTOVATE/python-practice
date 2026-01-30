#Write a program to check wethere a given number is prime or not?

# n = int(input("Enter the number :"))

# if n <= 1:
#     print("Not a prime")
# else:
#     for i in range(2,n):    
#         if n%i == 0:
#             print("Not a prime")
#             break
#     else:
#         print("PRIME")

n = int(input("Enter the number: "))

if n <= 1:
    print("Not a prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not a prime")
            break
    else:
        print("PRIME")









