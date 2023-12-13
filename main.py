def main():
    book_path = "/home/sonia_friesen/workspace/github.com/soniafriesen/bookbot/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)    
    print("-- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for char in chars_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {chars_dict[char]} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()