"""Example of a function that searches through a list."""

# Definiea function named contains
# two parameters:
# 1. needle - the string were searching for
# 2. haystack - the list were searching through


def main() -> None: 
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))


def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithm
    #  for each item in the haystack
    #   test if it is equal to the needl
    #       if so, return true
    for item in haystack:
        if item == needle:
            return True
#  after testing all items return false, because not found anywhere
# returns true if needle in haystack, flase other wise
    return False


if __name__ == "__main__":
    main()