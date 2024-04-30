import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
from app.books import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class SerializerJSON(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class SerializerXML(Serializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class SerializerBook:
    @staticmethod
    def serialize(book: Book, serialize_type: str) -> str:
        if serialize_type == "json":
            return SerializerJSON().serialize(book)
        elif serialize_type == "xml":
            return SerializerXML().serialize(book)
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
