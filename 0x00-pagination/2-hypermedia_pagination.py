import csv
import math
from typing import List


def index_range(page, page_size):
    """a function that returns the firdt and last index"""
    first_index = (page - 1) * page_size
    last_index = page * page_size
    return (first_index, last_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """a function that returns a specific page from the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        range = index_range(page, page_size)
        result = []
        data = self.dataset()
        if range[1] > len(data) or range[0] > len(data):
            return result
        else:
            return data[range[0]: range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """a method that takes the same arguments and
        returns a dictionary containing the information"""
        data = self.dataset()
        total_pages = math.ceil(len(data) / page_size)
        prev = page - 1 if page != 1 else None
        next = page + 1 if page < total_pages else None
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next,
            "prev_page": prev,
            "total_pages": total_pages
        }
