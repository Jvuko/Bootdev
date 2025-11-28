from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path = "/home/vukoj/BootDev/Bootdev/books/frankenstein.txt"
    text = get_book_text(path)
    words = count_words(text)
    char = count_chars(text)
    sorted = my_sort(char)

    print("============ BOOKBOT ============"
          "Analyzing book found at books/frankenstein.txt..."
          "----------- Word Count ----------"
          f" {words} total words"
          "--------- Character Count -------")
    for item in sorted:
        print(f"{item["char"]}: {item["num"]}\n")
    

main()