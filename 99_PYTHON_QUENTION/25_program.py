# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
# Notes
# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.



def conver_into_negative(num):
    if num > 0 :
        num *= -1 
        print(num)
    elif num < 0:
        print(f"the ({n}) is already negaive there is no need to change in negative.")
    else:
        print(f"Zero ({0}) is not checked for any specific sign. Negative zeros make no mathematical sense.")
      


    
n = int(input("Enter the numeber :"))

conver_into_negative(n)

