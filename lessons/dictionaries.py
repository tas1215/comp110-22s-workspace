"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# initialize to an empty dictionary
schools = dict()

# set a key value pairing to the dicitonary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print a dictonary literal representation
print(schools)

# access a value by its key -- lookup
print(f"UNC has {schools['UNC']} students")

# remove a key value pair from a dictionary
# by its key
schools.pop("Duke")

# test for existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in shcools")
else:
    print("No key 'Duke' in schools")

# update / reassignn a key value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# demonstraition of dictionary literals

# empty dictionary literal
schools = {}  # same as dict()

# alternatively, initialize key value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# what happens when a key does not exist? answer: key error
# print(schools["UNCC"])

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")