#write a python program to count all the vowels in a given string

# #logic 1 without declaring a variable
# str="Welcome to knowledge stream="
# x="aeiou"
# count=0
# for char in str:
#     if char in x:
#         count+=1 
# print("your vowel character is=",count)



#logic 2(with declaring a variable)
str=input("enter a string=")
count=0
vowels="aeiou"
for char in str:
    if char in vowels:
        count=count+1
print("you entered vowel character are=",count)