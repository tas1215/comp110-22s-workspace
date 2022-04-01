from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items
    
    def __repr__(self) -> str:
        return f"StrArray({self.items})"
    
    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Vectorized concatenation operator."""
        # Set up a result list of strings thats empty
        result: list[str] = []
        if isinstance(rhs, str):
            # loop through each item in self.items
            for item in self.items:
                # for each item, append the concatenation of item and rhs to result list
                result.append(item + rhs)
        else:
            # Assert that len of self.items is equal to length of rhs.items
            assert len(self.items) == len(rhs.items)
            # build up the result list by concatenating
            # each item in self.items with corresponding item in rhs.items
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
        # return a newly constructed StrArray whos items are result
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!"
print(result)
print(first + " " + last)
print(last + ", " + first)
