#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of a mxd list"""
    sum_mixed_list = sum(mxd_lst)
    return sum_mixed_list
