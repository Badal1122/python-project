# Write a function that merges two dictionaries.
# If a key is present in both dictionaries, the value from the second dictionary
# should be used.

def merge(a,b):
    return a|b
c={'a':1,'b':2,'c':3,'d':4}
d={'a':2,'b':4,'c':5,'d':8}
print(merge(c,d))