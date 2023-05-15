#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                
                self.__dataset = dataset[1:]
                return self.__dataset
    
    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting a
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
                    }
            return self.__indexed_dataset
    
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert index >= 0
        assert page_size >= 0
        c_index = index
        n_index = index + page_size
        p_size = page_size
        dat = []
        count = 0
        print(index, index + page_size)
        for i in range(index, index + page_size):
            if self.__indexed_dataset.get(i):
                dat.append(self.__indexed_dataset.get(i))
            else:
                count = count + 1
        print(count)
        if count:
            for i in range(index + page_size, index + page_size + count):
                if self.__indexed_dataset.get(i):
                    dat.append(self.__indexed_dataset.get(i))

        return ({'index': c_index, 'data': dat, 'page_size':p_size, 'next_index': n_index})
