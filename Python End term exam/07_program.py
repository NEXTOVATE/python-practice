# Write a function that takes a string and returns a new string containing only characters whose frequency is exactly equal to the median frequency of all characters. 

def median_frequency_string(s):
    from collections import Counter
    freq = Counter(s)
    frequencies = sorted(freq.values())
    n = len(frequencies)
    
    if n % 2 == 1:
        median_freq = frequencies[n // 2]
    else:
        median_freq = (frequencies[n // 2 - 1] + frequencies[n // 2]) / 2
    
    result = ''.join([char for char in s if freq[char] == median_freq])
    return result
