"""Unit test assignment."""

__author__ = "730312196"


def only_evens(evens: list[int]) -> list[int]:
    """This function will return the evens of a list."""
    i: int = 0
    list_of_evens: list[int] = []
    while i < len(evens):
        if evens[i] % 2 == 0:
            list_of_evens.append(evens[i])
        i += 1
    return list_of_evens


def sub(a_list: list[int], start_in: int, end_in: int) -> list[int]:
    """This will take a middle subset of the list."""
    i: int = 0
    sub_list: list[int] = []
    if len(a_list) == 0 or start_in > len(a_list) or end_in <= 0:
        return sub_list
    else:
        if start_in < 1:
            while i < len(a_list):
                sub_list.append(a_list[i])        
                i += 1
        else:
            if start_in >= 0:
                i += 1
                while i < len(a_list):
                    sub_list.append(a_list[i])
                    i += 1
        if end_in < len(a_list):
            sub_list.pop(len(sub_list) - 1)
    return sub_list


def concat(b_list: list[int], c_list: list[int]) -> list[int]:
    """This will return the two lists, but they are combined with each other."""
    combine_list: list[int] = []
    i: int = 0
    while i < len(b_list):
        combine_list.append(b_list[i])
        i += 1
    i = 0
    while i < len(c_list):
        combine_list.append(c_list[i])
        i += 1
    return combine_list