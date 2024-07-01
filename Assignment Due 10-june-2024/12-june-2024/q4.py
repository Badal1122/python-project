# Write a function that finds the key with the maximum value in a dictionary
d={'a':1,'b':2,'c':3}
def max_value(a):
    return max(a,key=a.get)
print(max_value(d))


    
