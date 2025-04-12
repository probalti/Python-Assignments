class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"{self.title} by {self.author} - {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully!")

    def show_books(self):
        if not self.books:
            print("Library is empty.")
            return
        print("\nBooks in Library:")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. ", end="")
            book.display()

    def borrow_book(self):
        self.show_books()
        if self.books:
            choice = int(input("Enter book number to borrow: "))
            if 1 <= choice <= len(self.books):
                book = self.books[choice - 1]
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You borrowed '{book.title}'.")
                else:
                    print("Book is already borrowed.")
            else:
                print("Invalid choice.")

    def return_book(self):
        self.show_books()
        if self.books:
            choice = int(input("Enter book number to return: "))
            if 1 <= choice <= len(self.books):
                book = self.books[choice - 1]
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"'{book.title}' has been returned.")
                else:
                    print("That book wasn't borrowed.")
            else:
                print("Invalid choice.")

    def run(self):
        while True:
            print("\n=== Library Menu ===")
            print("1. Add Book")
            print("2. Show All Books")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Exit")
            option = input("Choose an option (1-5): ")

            if option == '1':
                self.add_book()
            elif option == '2':
                self.show_books()
            elif option == '3':
                self.borrow_book()
            elif option == '4':
                self.return_book()
            elif option == '5':
                print("Exiting Library Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


# Start the program
lib = Library()
lib.run()
