from main import BooksCollector
import pytest

@pytest.fixture(autouse=True)
def books_collector():
    books_collector = BooksCollector()
    return books_collector


