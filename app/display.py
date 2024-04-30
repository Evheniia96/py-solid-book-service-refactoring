from abc import ABC, abstractmethod

from app.books import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class DisplayBook:
    @staticmethod
    def display(book: Book, display_type: str) -> None:
        if display_type == "console":
            DisplayConsole().display(book)
        elif display_type == "reverse":
            DisplayReverse().display(book)
        else:
            raise ValueError(f"Unknown display type: {display_type}")
