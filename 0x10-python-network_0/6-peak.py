#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""

    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid = len(list_of_integers) // 2
    if (list_of_integers[mid] > list_of_integers[mid - 1] and
            list_of_integers[mid] > list_of_integers[mid + 1]):
        return list_of_integers[mid]
    elif list_of_integers[mid] <= list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
