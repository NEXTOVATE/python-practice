# Write a function that returns both the minimum and maximum number of the given list/array.

# Examples (Input --> Output)
# [1,2,3,4,5] --> [1,5]
# [2334454,5] --> [5,2334454]
# [1]         --> [1,1]

def min_max(n):
   return [min(n),max(n)]             # after sort => return [n[0],n[-1]]

    
    



lst = [1,5,6,3,6]


x = min_max(lst)
print(x)
