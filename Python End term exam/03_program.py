# Given a list of integers, remove every element that is immediately followed by a smaller number. (Modify the list in-place, no extra list allowed.)

numbers = [5, 3, 8, 1, 4, 7]
i = 0
while i < len(numbers) - 1:
    if numbers[i] > numbers[i + 1]:
        del numbers[i]
    else:
        i += 1
print("Modified list:", numbers)

