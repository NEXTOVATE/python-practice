# Write a recursive function that returns the sum of all integers inside a nested list of arbitrary depth.
# Example: [1, [2, [3, 4], 5], 6] → 21
def sum_nested(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_nested(item)  # Recursive call for nested lists
        else:
            total += item  # Add integer to total
    return total
# Example usage
nested_list = [1, [2, [3, 4], 5], 6]
result = sum_nested(nested_list)
print("Sum of nested list:", result)
