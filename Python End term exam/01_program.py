# question : Write a one-line Python expression using any() and slicing that checks if a string contains two identical consecutive characters (like "tt" in "letter"). (1 Marks )

x = input("Enter a string: ")
result = any(x[i] == x[i+1] for i in range(len(x)-1))
print(result)
              