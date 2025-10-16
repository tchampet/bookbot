from stats import word_count, num_each_character, from_dict_to_sorted_list_of_dict
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    
    book = get_book_text(book_path)

    char_count_dict = num_each_character(book)

    nb_words = word_count(book)
    # print(f"Found {nb_words} total words")
    # print(char_count_dict)
    char_count = from_dict_to_sorted_list_of_dict(char_count_dict)
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {nb_words} total words
--------- Character Count -------""")
    for char_dict in char_count:
        if char_dict["char"].isalpha():
            char, num = char_dict["char"], char_dict["num"]
            print(f"{char}: {num}")
    print("============= END ===============")

main()