from stats import get_word_count, get_character_count, report
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_count = get_word_count(get_book_text(sys.argv[1]))
    character_count = get_character_count(get_book_text(sys.argv[1]))
    report(word_count, character_count, sys.argv[1])


main()
