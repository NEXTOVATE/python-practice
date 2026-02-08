# Without using [::-1], reversed(), or built-ins, write code to check whether a string is a palindrome using only loops and indexing
string = input("Enter a string: ")
is_palindrome = True
for i in range(len(string) // 2):
    if string[i] != string[len(string) - 1 - i]:
        is_palindrome = False
        break
print(f"{string} is a palindrome: {is_palindrome}")
