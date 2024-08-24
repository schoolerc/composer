import this
from typing import Iterator

DEFAULT_PAGE_SIZE = 10

class PageRequest:
    page: int
    page_size: int

class Page[T]:
    content: list[T]
    page: int
    total_elements: int
    total_pages: int

    def __init__(self, content, page, total_elements, total_pages):
        self.content = content
        self.page = page
        self.total_elements = total_elements
        self.total_pages = total_pages

    def __iter__(self) -> Iterator[T]:
        return iter(self.content)

    def __len__(self) -> int:
        return len(self.content)
