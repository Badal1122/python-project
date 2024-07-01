#find and print the common elements between two lists

#logic 1 using loop to print the common elements between two lists

# list3=[1,20,30,50,60]
# list4=[1,20,60,8,9]
# common_elements=[]
# for i in list3:
#     if i in list4:
#         common_elements.append(i)
# print(common_elements)


#logic 2 using interseection method to print the common elements bewtween two lists 

list3=[1,20,30,50,60]
list4=[1,20,60,8,9]
common_elements=list(set(list3).intersection(list4))
print(common_elements)