from abc import ABC, abstractmethod

# SRP — Book class stores only book-related data
class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

# ISP — LibraryInterface defines specific methods required for working with a library
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def get_books(self) -> list[Book]:
        pass

# OCP, LSP — Library implements the interface and can be substituted without breaking functionality
class Library(LibraryInterface):
    def __init__(self):
        self._books: list[Book] = []

    def add_book(self, book: Book):
        self._books.append(book)

    def remove_book(self, title: str):
        self._books = [book for book in self._books if book.title != title]

    def get_books(self) -> list[Book]:
        return self._books

# DIP — LibraryManager depends on abstraction (LibraryInterface) rather than a concrete implementation
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        books = self.library.get_books()
        if not books:
            print("No books in the library.")
        else:
            for book in books:
                print(book)

def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
