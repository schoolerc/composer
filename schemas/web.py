import this
from typing import Iterator, Any, Annotated

from fastapi import Depends
from pydantic import BaseModel

DEFAULT_PAGE_SIZE = 10


class PageRequest:
    def __init(self, page_number: int = 0, page_size: int = DEFAULT_PAGE_SIZE):
        self.page_number = page_number
        self.page_size = page_size


PageRequestDep = Annotated[dict, Depends(PageRequest)]


class Page[T](BaseModel):
    content: list[T]
    page: int
    total_elements: int
    total_pages: int

    def __init__(self, content, page, total_elements, total_pages, **data: Any):
        super().__init__(**data)
        self.content = content
        self.page = page
        self.total_elements = total_elements
        self.total_pages = total_pages

    def __iter__(self) -> Iterator[T]:
        return iter(self.content)

    def __len__(self) -> int:
        return len(self.content)
