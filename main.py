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

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")
    char_dictionary = get_char_count(text)
    print(char_dictionary)


main()