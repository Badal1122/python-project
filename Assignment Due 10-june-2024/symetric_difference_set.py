# Create a function symmetric_difference_sets that takes two sets and returns their
# symmetric difference. Explain with an example where you have two sets of users
# who attended different webinars. Find out who attended only one of the webinars.


def symmetric_difference_sets(set1,set2):
    sym_diff=set1.symmetric_difference(set2)
    return sym_diff

set3={"adil","raza","shoaib","Ali raza"}
set4={"Charlie","David","Eve","Frank","adil","raza"}
print(symmetric_difference_sets(set3,set4))
