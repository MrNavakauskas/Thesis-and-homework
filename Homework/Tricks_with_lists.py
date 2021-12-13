# Create an application that:
# • Should have a class Man, with the attribute name and age
# • There would be a repr method in the class that would represent the name and age
# • Initiate multiple Human objects with names and ages
# • Add created Human objects to a new list
# • Sort and print list items by name and age (and backwards)

from operator import attrgetter


class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return (f"({self.name}, {self.age})")


m1 = Man("Gediminas", 32)
m2 = Man("John", 22)
m3 = Man("Anton", 42)

list = [m1, m2, m3]

sort_by_name = sorted(list, key=attrgetter("name"))
print(sort_by_name)

sort_by_name_back = sorted(list, key=attrgetter("name"), reverse=True)
print(sort_by_name_back)

sort_by_age = sorted(list, key=attrgetter("age"))
print(sort_by_age)

sort_by_age_back = sorted(list, key=attrgetter("age"), reverse=True)
print(sort_by_age_back)