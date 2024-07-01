# Write a function is_superset that takes two sets and returns True if the first set
# is a superset of the second set, and False otherwise. Use this to determine if the
# set of all registered voters is a superset of the set of people who voted in an
# election.


def is_superset(set1,set2):
    is_superset=set1.issuperset(set2)
    return is_superset
set3 = {"f", "e", "d", "c", "b", "a"}
set4 = ["a", "b", "c"]
print(is_superset(set3,set4))