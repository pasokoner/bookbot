def main():
    book_path = "books/frankenstein.txt"
    content = get_text(book_path)
    words = count_words(content) 
    chars = get_chars_count(content)
    print_report(book_path, words, chars)

def get_chars_count(text):
    chars = {}
    for letter in text.lower():
        if letter in chars:
            chars[letter] += 1
            continue
        chars[letter] = 1
    return chars

def count_words(text):
    return len(text.split())

def get_text(path):
    with open(path) as f:
        return f.read()

def print_report(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} found in the document")
    
    chars_list = []
    for k, count in chars.items():
        chars_list.append({ "char": k, "count": count })

    chars_list.sort(reverse=True, key=sort_on)
    for c in chars_list:
        if c["char"].isalpha():
            print(f"The '{c["char"]}' was found {c["count"]} times")

    print("--- End report ---")

    
def sort_on(dict):
    return dict["count"]


main()