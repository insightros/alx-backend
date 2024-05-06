#!/usr/bin/env python3
"pagination help function"
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    "retrieves index"
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
