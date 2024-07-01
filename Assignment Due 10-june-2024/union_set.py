# Create a function union_sets that takes two sets and returns their union.
# Provide an example with two sets representing students enrolled in two different
# courses and find out the total number of unique students


def union_set(set1,set2):
    uni_std=set1.union(set2)
    return uni_std
set3={"adil","raza","shoaib","Ali raza"}
set4={"Charlie","David","Eve","Frank","adil","raza"}
print(union_set(set3,set4))





