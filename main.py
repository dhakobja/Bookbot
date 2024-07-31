def count_words(text):
    number_of_words = len(text.split())
    return number_of_words

def character_count(text):
    character_count = {}
    for character in text.lower():
        if character.isalpha():
            character_count[character] = character_count.get(character, 0) + 1
    return character_count

def main():
    book_path = 'books/frankenstein.txt'

    with open(book_path, 'r') as file:
        Book = file.read()
        
    number_of_words = count_words(Book)

    number_of_characters = character_count(Book)
    number_of_characters_sorted = sorted(number_of_characters.items(), key=lambda item: item[1], reverse=True)

    print(f"--- Begin report of {book_path} ---")
    print(f'{number_of_words} words found in the document')

    for character, count in number_of_characters_sorted:
        print(f"The '{character}' character was found {count} times")
    
    print(f"--- End report ---")


if __name__ == '__main__':
    main()