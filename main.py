from stats import *
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    words = count_words(text)
    char = count_chars(text)
    sorted = my_sort(char)

    print("============ BOOKBOT ============"
          f"Analyzing book found at {sys.argv[1]}"
          "----------- Word Count ----------"
          f" {words} total words"
          "--------- Character Count -------")
    for item in sorted:
        print(f"{item["char"]}: {item["num"]}\n")
    

main()