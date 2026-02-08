# Write Python code to find all substrings of length ≥ 2 that contain only unique characters.
# Example: "abca" → "ab", "abc", "bc", "ca"

string = input("Enter the string: ")
substrings = set()
for i in range(len(string)):
    for j in range(i + 2, len(string) + 1):
        substring = string[i:j]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
print("Unique character substrings of length ≥ 2:", substrings)

