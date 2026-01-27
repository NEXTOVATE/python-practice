# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]


def each_value_double(arry):
    new_arry = []
    for i in arry:
        new_arry.append(i*2)
    return new_arry
    



arry = [2,3,4]





print(each_value_double(arry))