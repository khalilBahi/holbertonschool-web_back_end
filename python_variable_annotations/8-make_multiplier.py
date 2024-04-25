#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier"""

    def make_a_multiplier(number: float) -> float:
        """returns a function that multiplies a float by multiplier"""
        return number * multiplier

    return make_a_multiplier
