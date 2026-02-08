# Write a Python program that:

# Accepts a paragraph as input.

# Manually splits the paragraph into sentences using ., !, and ?.

# For each sentence, compute:

# Number of words
# Number of uppercase letters
# Ratio of vowels to total characters
# Output Requirements:

# Print the sentence with:

# Highest word count
# Maximum uppercase letters
# Highest vowel ratio
# Also print the index of each corresponding sentence.

paragraph = input("Enter a paragraph: ")
sentences = []
current_sentence = ""
for char in paragraph:
    current_sentence += char
    if char in ['.', '!', '?']:
        sentences.append(current_sentence.strip())
        current_sentence = ""
max_word_count = 0
max_uppercase_count = 0
max_vowel_ratio = 0
index_max_word_count = 0
index_max_uppercase_count = 0
index_max_vowel_ratio = 0
for index, sentence in enumerate(sentences):
    words = sentence.split()
    word_count = len(words)
    uppercase_count = sum(1 for char in sentence if char.isupper())
    vowel_count = sum(1 for char in sentence if char.lower() in 'aeiou')
    total_characters = len(sentence)
    vowel_ratio = vowel_count / total_characters if total_characters > 0 else 0
    if word_count > max_word_count:
        max_word_count = word_count
        index_max_word_count = index
    if uppercase_count > max_uppercase_count:
        max_uppercase_count = uppercase_count
        index_max_uppercase_count = index
    if vowel_ratio > max_vowel_ratio:
        max_vowel_ratio = vowel_ratio
        index_max_vowel_ratio = index
print(f"Sentence with highest word count: '{sentences[index_max_word_count]}' (Index: {index_max_word_count})")
print(f"Sentence with maximum uppercase letters: '{sentences[index_max_uppercase_count]}' (Index: {index_max_uppercase_count})")
print(f"Sentence with highest vowel ratio: '{sentences[index_max_vowel_ratio]}' (Index: {index_max_vowel_ratio})")
