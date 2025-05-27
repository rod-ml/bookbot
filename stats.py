def get_word_count(book_text):
    words = book_text.split()
    return len(words)


def get_character_count(book_text):
    characters = {}
    for char in book_text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters


def report(word_count, characters, filepath):
    sorted_characters = sorted(
        characters.items(), key=lambda item: item[1], reverse=True
    )

    print(f"""
============ BOOKBOT ============\n
Analyzing book found at {filepath}... \n
----------- Word Count ---------- \n
Found {word_count} total words\n
--------- Character Count -------\n
          """)

    for char, count in sorted_characters:
        print(f"{char}: {count}")

    print("============= END ===============")
