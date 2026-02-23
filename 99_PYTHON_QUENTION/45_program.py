# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]


# arry = []
# while n > 0:
#     arry.append(n)
#     n -=1
# print(arry)


def reverse_arry(n):
    arry = []
    while n > 0:
        arry.append(n)
        n -=1
    return arry







n = int(input("enter the number :"))

print(reverse_arry(n))



