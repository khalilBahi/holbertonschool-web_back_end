#!/usr/bin/env python3
"""Complex types - list of floats"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    return sums of elements in the list 
    """
    sum = 0
    for i in input_list:
        sum += i
    return sum
