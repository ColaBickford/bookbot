from stats import get_num_words, character_repeat_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        franken_text = get_book_text(sys.argv[1])
        total_words = get_num_words(franken_text)
        word_count = character_repeat_count(franken_text)
        print(r"============ BOOKBOT ============")
        print(r"Analyzing book found at books/frankenstein.txt...")
        print(r"----------- Word Count ----------")
        print(f"Found {total_words} total words")
        print(r"--------- Character Count -------")
        for char, count in word_count:
            print(f"{char}: {count}")
        print(r"============= END ===============")


if __name__ == "__main__":
    main()