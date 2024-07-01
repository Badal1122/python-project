# Define a function is_subset that takes two sets and returns True if the first set
# is a subset of the second set, and False otherwise. Use this to check if a group
# of students (set A) is a subset of the entire class (set B).


def is_subset(set1,set2):
    issubset=set1.issubset(set2)
    return issubset
set3={"adil","raza","shoaib","Ali raza"}
set4={"Charlie","David","Eve","Frank","adil","raza"}
 #False means set 1 all values not apperaed in set 2 
# print(is_subset(issubset))
print(is_subset(set3,set4))

