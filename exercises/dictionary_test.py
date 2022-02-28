"""Test for Dictionary."""

__author__ = "730312196"


from dictionary import invert
import pytest
from dictionary import favorite_color
from dictionary import count


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


def test_favorite_color_use2() -> None:
    """Use test 2 for favorite_color function."""
    color_dict: dict[str, str] = {'tyler': 'blue', 'wes': 'white', 'grant': 'blue', 'mason': 'green', 'baird': 'white', 'hobbs': 'white'}
    assert favorite_color(color_dict) == "white"


def test_favorite_color_edge() -> None:
    """Edge test for favorite_color function."""
    color_dict: dict[str, str] = {'tyler': 'blue'}
    assert favorite_color(color_dict) == 'blue'


def test_count_use1() -> None:
    """Use test 1 for count function."""
    a_list: list[str] = ["blue", "blue", "blue", "green", "green", "white"]
    assert count(a_list) == {'blue': 3, 'green': 2, 'white': 1}