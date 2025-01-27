def sort_on(dict):
    return dict["num"]

def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)
    word_count = get_word_count(book)
    char_count = get_char_count(book)
    print(f"--- Start report of {book_path} ---")
    print(f"{word_count} words found in entire book\n")
    
    for char_dict in char_count:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    
    print("---End Report---")
    
def get_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(book):   
    words = len(book.split())
    return words

def get_char_count(book):
    characters = {}
    lowered_book = book.lower()
    for i in lowered_book:
        if i.isalpha():
            if i in characters:
                characters[i] += 1                
            else:
                characters[i] = 1
    char_list = []
    for char, num in characters.items():
        char_dict = {"char": char, "num": num}
        char_list.append(char_dict)
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

   
if __name__ == "__main__":
    main()