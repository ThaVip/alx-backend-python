#!/usr/bin/env python3
"""
This module provides a function to sum a list of floats.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of all elements in the list.
    """
    return sum(input_list)

