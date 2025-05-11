from abc import ABC, abstractmethod
from typing import List
import logging

# Cтворюємо логер, рівень INFO
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


# Виконується принцип єдиної відповідальності (SRP), клас Book відповідає за зберігання інформації про книгу
class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Виконується принцип відкритості/закритості (OCP), клас Library міг бути розширений для нової функціональності без зміни коду.
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


# Принцип підстанови Лісков (LSP), будь-який клас, який наслідує інтерфейс LibraryInterface, може замінити клас Library без порушення роботи програми.
# Використовується інтерфейс LibraryInterface для чіткої специфікації методів, які необхідні для роботи з бібліотекою library
class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books[:] = [book for book in self.books if book.title != title]

    def get_books(self) -> List[Book]:
        return self.books


# Виконується принцип інверсії залежностей (DIP), класи вищого рівня, такі як LibraryManager, залежали від абстракцій (інтерфейсів), а не від конкретних реалізацій класів
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logger.info(f"Added book: {book}")

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        logger.info(f"Removed book: {title}")

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            logger.info("No books in the library.")
        else:
            for book in books:
                logger.info(str(book))


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
                logger.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
