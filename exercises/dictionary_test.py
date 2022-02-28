"""Test for Dictionary."""

__author__ = "730312196"


from dictionary import invert
import pytest
from dictionary import favorite_color


def test_invert_use1() -> None:
    """Use Test 1 for invert function."""
    a_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use2() -> None:
    """Use Test 2 for invert function. This one checks for the key error."""
    with pytest.raises(KeyError):
        a_dict: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
        invert(a_dict)


def test_invert_edge() -> None:
    """Edge Test for invert function."""
    a_dict: dict[str, str] = {}
    assert invert(a_dict) == {}


def test_favorite_color_use1() -> None:
    """Use Test 1 for favorite_color funciton."""
    color_dict: dict[str, str] = {'Marc': 'yellow', 'Ezri': 'blue', 'Kris': 'blue'}
    assert favorite_color(color_dict) == "blue"