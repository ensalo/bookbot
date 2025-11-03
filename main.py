import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

from stats import count_words, count_chars, sort_characters


def main():
    if len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        location = sys.argv[1]
        contents = get_book_text(location)
        count = count_words(contents)
        chars = count_chars(contents)
        sorted_chars = sort_characters(chars)
    
        print("============ BOOKBOT ============")
        print(f"Analysing book found at {location}...")
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        for item in sorted_chars:
            if not item["char"].isalpha():
                continue
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

main()