def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_dictionary = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1

    return char_dictionary

def sort_on(dict):
    return dict["total"]

def convert_dict_to_list(char_dictionary):
    char_list = []
    for entry in char_dictionary:
        if (entry.isalpha()):
            char_list.append({"char": entry, "total": char_dictionary[entry]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def print_report(book_path, char_dictionary, word_count):
    char_list = convert_dict_to_list(char_dictionary)

    print(f"--- Begin report of {book_path}")
    print(f"{word_count} words found in the document")
    print("")

    for char_entry in char_list:
        print(f"The character '{char_entry['char']}' was found {char_entry['total']} times")

    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_dictionary = get_char_count(text)
    print_report(book_path, char_dictionary, word_count)

main()
