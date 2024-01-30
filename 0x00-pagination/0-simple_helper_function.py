#!/usr/bin/env python3
"""
simple_helper_function
"""


def index_range(page, page_size):
    """a function that returns the firdt and last index"""
    first_index = (page - 1) * page_size
    last_index = page * page_size
    return (first_index, last_index)
