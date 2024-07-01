
# Write a function that takes a list of integers and returns a dictionary with the
# frequency count of each element.
list1=[1,2,3,4,5,5]
dict2={}
def dict1(list1):
    for i in list1:
       t=list1.count(i)
       dict2[i]=t
    return dict2
print(dict1(list1))



    
    

