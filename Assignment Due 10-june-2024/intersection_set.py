# Define a function intersection_sets that takes two sets and returns their
# intersection.Use this function to find common members in two different clubs
# in a school.

def intersection_sets(set1,set2):
    inter_set=set1.intersection(set2)
    return inter_set
set3={"Anna","Ben","Clara","Daniel"}
set4=["Adil","Ben","Daniel","sial"]
print(intersection_sets(set3,set4))
