#- Count how many numbers in a list are greater than a given value.
# list5=[1,5,8,9,12,3,14,25]
# given_value=5
# count=0
# for i in list5:
#     if i>given_value:
#         print(i)
#         count=count+1
# print(count)


list6=[1,20,25,26,27,28,30]
given_value=12
count=0
i=0
while i <len(list6):
    if list6[i]>given_value:
        print(list6[i])        
        count=count+1
    i=i+1
print(count)