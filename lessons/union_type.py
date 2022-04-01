"""An example of union types."""

from typing import Union


def log(info: Union[int, str] = "OhNo") -> None:
    """Log is a function that can be called with _either_ an int or an str arguement."""
    if isinstance(info, str):
        print(f"str: {info.lower()}")
    else:
        print(f"int: {info}")


log()
log("Hello, World")
log(110)