# Write a Python program to left-rotate a list by k positions without using slicing or extra lists, only by shifting elements manually.
def left_rotate(lst, k):
    n = len(lst)
    k = k % n  # Handle cases where k is greater than n
    for _ in range(k):
        first_element = lst[0]
        for i in range(1, n):
            lst[i - 1] = lst[i]
        lst[n - 1] = first_element
    return lst