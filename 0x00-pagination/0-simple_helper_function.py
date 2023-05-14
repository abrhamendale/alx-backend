#!/usr/bin/env python3
"""
Pagination
"""


def index_range(page, page_size):
    """
    Returns the start and end of an index.
    """
    start = page_size * (page - 1)
    end = start + page_size
    return ((start, end))
