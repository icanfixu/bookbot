from stats import get_num_words, get_num_chars, get_dic_char
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(get_book_text(book_path))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = get_dic_char(get_num_chars(get_book_text(book_path)))
    for i in num_chars:
        char = i["char"]
        num = i["num"]
        if char.isalpha():
            print(f'{char}: {num}')
    print("============= END ===============")


main()

