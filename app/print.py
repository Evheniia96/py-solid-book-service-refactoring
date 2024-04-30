from abc import ABC, abstractmethod

from app.books import Book


class Print(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class PrintConsole(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(Print):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrintBook:
    @staticmethod
    def print_book(book: Book, print_type: str) -> None:
        if print_type == "console":
            PrintConsole().print_book(book)
        elif print_type == "reverse":
            PrintReverse().print_book(book)
        else:
            raise ValueError(f"Unknown print type: {print_type}")
