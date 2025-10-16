from stats import word_count, num_each_character


def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text 

def main():
    book = get_book_text("./books/frankenstein.txt")
    char_count_dict = num_each_character(book)

    nb_words = word_count(book)
    print(f"Found {nb_words} total words")
    print(char_count_dict)
main()