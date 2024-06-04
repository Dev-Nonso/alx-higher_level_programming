#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""

def find_peak(list_of_integers):
    """
    Function to find a peak in a list of unsorted integers.
    Args:
        list_of_integers (list): List of integers.
    Returns:
        int: Peak value.
    """
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
