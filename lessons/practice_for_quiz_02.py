"""Practice for quiz 02."""


def odd_and_even(a_list: list[int]) -> list[int]:
    """Returns a list of odds that had an even index."""
    i: int = 0
    b_list: list[int] = []
    while i < len(a_list):
        if a_list[i] % 2 != 0:
            b_list.append(a_list[i])
            i += 2
        else:
            i += 2
    return b_list


def vowels_and_threes(a_str: str) -> str:
    """Returns chars that are multiples of three or a vowel."""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    new_str: str = ""
    is_vowel: bool = False
    i: int = 0
    j: int = 0
    while i < len(a_str):
        is_vowel = False
        j = 0
        while j < len(vowels):
            if vowels[j] == a_str[i]:
                is_vowel = True
            j += 1
        if is_vowel and i % 3 == 0:
            # nothing
            new_str += ""
            i += 1
        elif i % 3 != 0:
            new_str += vowels[j]
            i += 1
        elif is_vowel:
            new_str += a_str
            i += 1
    return new_str


def avg_grades(a_dict: dict[str, list[int]]) -> dict[str, float]:
    """Diict that maps to studnts average."""
    new_dict: dict[str, float] = {}
    for key in a_dict:
        total: int = 0
        for grade in a_dict[key]:
            total += grade
        new_dict[key] = total / len(a_dict[key])
    return new_dict