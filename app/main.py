from app.books import Book
from app.display import DisplayBook
from app.print import PrintBook
from app.serializers import SerializerBook


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DisplayBook.display(book,method_type)
        elif cmd == "print":
            PrintBook.print_book(book, method_type)
        elif cmd == "serialize":
            return SerializerBook.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
