"""This is the Dictionary assignment."""

__author__ = "730312196"


def invert(a_dict: dict[str, str]) -> dict[str, str]:
    """Invert the dictionary by switching the values and keys."""
    inverted_dict: dict[str, str] = {}
    for key in a_dict:
        if a_dict[key] in inverted_dict:
            raise KeyError()
        inverted_dict[a_dict[key]] = key
    return inverted_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the most popular favorite color. If there is a tie then the first color returns."""
    most_pop_color: str = ""
    new_dictionary: dict[str, int] = {}
    for key in color_dict:
        if color_dict[key] in new_dictionary:
            new_dictionary[key] += 1
        else:
            new_dictionary[key] = 1
    i: int = 0
    for key in new_dictionary:
        if new_dictionary[key] > i:
            i += 1
        else:
            most_pop_color = color_dict[key]
    return most_pop_color
