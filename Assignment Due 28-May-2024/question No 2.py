#Find the maximum and minimum elements in a list.

#logic 1 without using a loop 

# list1=[20,45,30,36]
# print(min(list1))
# print(max(list1))


#logic 2 using for loop without range 

# list2=[1,3,5,10,20,25]
# min_number=list2[0]
# max_number=list2[0]
# for i in list2[1:]:
#     if (i<min_number):
#         min_number=i
#     if (i>max_number):
#         max_number=i
# print(min_number)
# print(max_number)


#logic 3 using for loop with range to find max number in the list not index 

# list2=[1,25,30,50,50,51,36]
# min_number=list2[0]
# max_number=list2[0]
# for i in range(1,len(list2)):
#     if list2[i]<min_number:
#         min_number=list2[i]
#     if list2[i]>max_number:
#         max_number=list2[i]
# print(max_number)
# print(min_number)


#4 logic 4 using while loop to find max and min number in the list not find index 

list3=[20,34,45,67,89,99,120]
min_number=list3[0]
max_number=list3[0]
i=1
while i<len(list3):
    if list3[i]<min_number:
        min_number=list3[i]
    if list3[i]>max_number:
        max_number=list3[i]
        i=i+1
print(min_number)
print(max_number)
