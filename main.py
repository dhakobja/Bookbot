def main():
    book_path = 'books/frankenstein.txt'

    with open(book_path, 'r') as file:
        Book = file.read()
        print(Book)

if __name__ == '__main__':
    main()