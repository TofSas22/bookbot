def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count_dict = count_characters(text) 

    print(f"--- Begin report of {book_path} ---")
    print(f"word count: {word_count}")
    print()
    print_report(char_count_dict)
    print()
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    count = 0
    words = string.split()
    # could have also put len(words) here to be concise and efficient
    for word in words:
        count += 1
    
    return count

def count_characters(string):
    char_dict = {}

    for char in string:
        char = char.lower()
        
        if char.isspace():
            continue
        elif char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def print_report(dict):
    sorted_chars = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    for char, num in sorted_chars:
        print(f"The {char} character was found {num} times.")

main()