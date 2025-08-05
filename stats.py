def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def sort_on(chars):
    return chars["num"]

def get_chars(file_contents):
    chars_dict = {};    
    chars_list = []

    for char in file_contents.lower():
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    
    for char in chars_dict:
        new_char = {"char": char, "num": chars_dict[char]}
        chars_list.append(new_char)

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list