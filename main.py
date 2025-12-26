import sys
from stats import get_num_words, get_letter_occurrence, get_sorted_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
#    file_path = "./books/frankenstein.txt"
#   Checking Sys' input
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    book_words = get_book_text(file_path)
    word_count = get_num_words(book_words)
    sorted_list_of_dict = get_sorted_dict(get_letter_occurrence(book_words))
#
# Printing out
#
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_list_of_dict:
        print(f"{dict["char"]}: {dict["num"]}")
main()