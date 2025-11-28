# Write a new function that accepts the text from the book as a string, and returns the number of words in the string. 
# The .split() method will be helpful here.
# Instead of printing the books contents, print this message to the console: Found {num_words} total words

def count_words(text):
    return f"Found {len(text.split())} total words"

# Add a new function to your stats.py file that takes the text from the book as a string, and 
# returns the number of times each character, (including symbols and spaces), appears in the string.
# Convert any character to lowercase using the .lower() method, we don't want duplicates.
# Use a dictionary of String -> Integer.

def count_chars(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

# Add a new function to your stats.py file that takes the dictionary of characters and their counts and 
# returns a sorted list of dictionaries.
# Each dictionary should have two key-value pairs: one for the character itself and one for that character's count 
# (e.g. {"char": "b", "num": 4868}).
# Use the .sort() method: Sort the list from greatest to least by the count.


def sort_on(items):
    return items["num"]

def my_sort(items: dict):
    sorted = []
    for k, v in items.items():
        if k.isalpha():
            sorted.append({"char" : k, "num" : v})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

