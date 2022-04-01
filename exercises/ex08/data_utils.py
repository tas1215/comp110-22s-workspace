"""Dictionary related utility functions."""

__author__ = "730312196"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the csv data and put it into rows that are represented by a dict of str."""
    result: list[dict[str, str]] = []
  
    # Open a handle to the date file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # read each row of the csv line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we are done, to free its resources.
    file_handle.close()

    return result


def column_values(columntable: list[dict[str, str]], title: str) -> list[str]:
    """Produce a list of strings of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in columntable:
        item: str = row[title]
        result.append(item)
    return result


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table as rows into a dictionary of columns."""
    result: dict[str, list[str]] = {}
    row_one: dict[str, str] = rows[0]
    for name in row_one:
        result[name] = column_values(rows, name)
    return result


def head(one_dict: dict[str, list[str]], x: int) -> dict[str, list[str]]:
    """Produce a new column-based table with x number of rows for each column."""
    result: dict[str, list[str]] = {}
    for column in one_dict:
        if x > len(one_dict[column]):
            return one_dict
        i: int = 0 
        store_list: list[str] = []
        while i < x:
            store_list.append(one_dict[column][i])
            i += 1
        result[column] = store_list 
    return result


def select(one_dict: dict[str, list[str]], sub: list[str]) -> dict[str, list[str]]:
    """Produce a new column based table with a subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in sub:
        result[column] = one_dict[column]
    return result


def concat(one_dict: dict[str, list[str]], two_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two column based dicts into one column based dict."""
    result: dict[str, list[str]] = {}
    for column in one_dict:
        result[column] = one_dict[column]
    for column in two_dict:
        if column in result:
            result[column] += two_dict[column]
        else:
            result[column] = two_dict[column]    
    return result


def count(a_list: list[str]) -> dict[str, int]:
    """Given a list of strings produce a dict where the keys are counted up."""
    result: dict[str, int] = {}
    for key in a_list:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result


def pop_rating(a_dict: dict[str, int]) -> str:
    """Given a dictionary that is created by the count function, return a str of the highest amount of votes per rating."""
    high_key: str = ""
    int_hightest: int = 0
    for key in a_dict:
        if a_dict[key] > int_hightest:
            int_hightest = a_dict[key]
            high_key = key
    return high_key