"""Test for utils."""

__author__ = "730312196"

from utils import concat
from exercises.ex05.utils import sub
from utils import only_evens


def test_only_evens() -> None:
    evens: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(evens) == [2, 4, 6]


def test_sub() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    start_in: int = 1
    end_in: int = 3
    assert sub(a_list, start_in, end_in) == [20, 30]


def test_concat() -> None:
    b_list: list[int] = [1, 2, 3, 4]
    c_list: list[int] = [1, 2, 3, 4]
    assert concat(b_list, c_list) == [1, 2, 3, 4, 1, 2, 3, 4]