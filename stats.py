def word_count(text):
    words = text.split()
    return len(words)

def num_each_character(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def from_dict_to_sorted_list_of_dict(char_dict):
    list_char = []
    for char, num in char_dict.items():
        list_char.append({"char": char, "num": num})
    list_char.sort(reverse=True, key=sort_on)
    return list_char


