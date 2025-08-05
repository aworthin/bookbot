import sys
from stats import count_words, get_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookfile=sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookfile}...")
   
    book_text = get_book_text(bookfile)
   
    num_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    sorted_chars = get_chars(book_text)
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        num = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

main()
