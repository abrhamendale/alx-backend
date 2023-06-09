#!/usr/bin/env python3
"""
Pagination task_1
"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def index_range(page, page_size):
        """
        Returns the start and end of an index.
        """
        start = page_size * (page - 1)
        end = start + page_size
        return ((start, end))

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page."""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        i = Server.index_range(page, page_size)
        ls = []
        if self.dataset() is None:
            return ([])
        end_index = i[1]
        if i[0] < 0 or i[0] > len(self.dataset()):
            return ([])
        if i[1] > len(self.dataset()):
            end_index = len(self.dataset())
        for j in range(i[0], end_index):
            if (self.dataset())[j]:
                ls.append((self.dataset())[j])
        return (ls)
