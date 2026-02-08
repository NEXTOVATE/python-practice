# Write Python code to deeply compare two dictionaries and return a dictionary showing only the differing keys and their values from both dictionaries.
# Rules:
# If values are dictionaries → compare recursively
# If values differ → store both values in a tuple (val1, val2)
def deep_compare_dicts(dict1, dict2):
    result = {}
    all_keys = set(dict1.keys()) | set(dict2.keys())
    
    for key in all_keys:
        val1 = dict1.get(key)
        val2 = dict2.get(key)
        
        if isinstance(val1, dict) and isinstance(val2, dict):
            nested_diff = deep_compare_dicts(val1, val2)
            if nested_diff:
                result[key] = nested_diff
        elif val1 != val2:
            result[key] = (val1, val2)
    
    return result
#Example usage
dict_a = {
    'name': 'Alice',
    'age': 30,
    'address': {
        'city': 'New York',
        'zip': '10001'
    }
}
dict_b = {
    'name': 'Alice',
    'age': 31,
    'address': {
        'city': 'Los Angeles',
        'zip': '90001'
    }
}
differences = deep_compare_dicts(dict_a, dict_b)
print("Differences between dictionaries:", differences)
    