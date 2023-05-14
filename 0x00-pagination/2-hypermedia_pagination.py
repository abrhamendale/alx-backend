#!/usr/bin/env python3
"""
Pagination task_1
"""


import csv
import math
from typing import List
import math


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        i = Server.index_range(page, page_size)
        ls = []
        if i[0] < 0 or i[1] >= len(self.dataset()):
            return ([])
        for j in range(i[0], i[1]):
            ls.append((self.dataset())[j])
        return (ls)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns info about the list."""
        dct = dict()
        lst = self.get_page(page, page_size)
        p_size = len(lst)
        _p = page
        d = lst
        if page + 1 < len(self.dataset()):
            n_page = page + 1
        else:
            n_page = None
        if page - 1 > 0:
            p_page = page - 1
        else:
            p_page = None
        if p_size:
            t_pages = round(len(self.dataset()) / p_size)
        else:
            t_pages = len(self.dataset())
        return ({"page_size": p_size, "page": _p, "data": d, "next_page":
                n_page, "prev_page": p_page, "total_pages": t_pages})
