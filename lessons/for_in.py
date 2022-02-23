"""An example of for in syntax."""

names: list[str] = ["Tyler", "Wes", "Mason", "Grant"]

# example of iteratin through names using a while loops
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# the following for...in loop iis the same as the whiile loop
for name in names:
    print(name)