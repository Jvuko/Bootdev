# Write a new function that accepts the text from the book as a string, and returns the number of words in the string. 
# The .split() method will be helpful here.
# Instead of printing the books contents, print this message to the console: Found {num_words} total words

def count_words(text):
    return f"Found {len(text.split())} total words"

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path = "/home/vukoj/BootDev/Bootdev/books/frankenstein.txt"
    text = get_book_text(path)
    res = count_words(text)
    print(res)

main()