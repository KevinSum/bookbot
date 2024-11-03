def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_text_word_count(text)
    chars_dict = get_chars_dict(text)

    print(f"{word_count} words found in the document")
    for key in chars_dict:
            print(f"The '{key}' character was found {chars_dict[key]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_text_word_count(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    dict = {}
    for char in text:
        char = char.lower()
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

main()