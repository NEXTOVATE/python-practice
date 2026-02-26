# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

# lines = ["a", "b", "c"]
# n = 0

# for i in lines:
#     n += 1
#     i.join()
#     i.replace
#     # arry1
# print(lines)
    
 

lines = ["a", "b", "c","d"]

result = []
for i in range(len(lines)):
    num = f"{i+1}: {lines[i]}"
    result.append(num)
print(result)



