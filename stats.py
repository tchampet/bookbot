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
