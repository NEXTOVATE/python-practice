n = int(input("Enter a number :"))
for i in range(0,11):
    if(i > 0):
        # i = i+i
        print(f"{n} x {11-i} = {n*(11-i)}")