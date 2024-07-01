# Write a function that inverts a dictionary (i.e., swap keys and values).
# Assume all values are unique.

def inver_dic(dict2):
    for key,value in dict2.items():
        c[value]=key
    return c
c={}
dict3={'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(inver_dic(dict3))
