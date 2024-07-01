#write a python program to count all the uppercase in a given string.....


# logic 1 without declaring a string
str="I Love Pakistan. I Am Very proud of My Country. My Country give me everything which i need."
count=0
for char in str:
    if char.isupper():
        count=count+1
print("your entered uppercase character are=",count)



#logic 2 With Declaring a string

str=input("enter a string=")
count=0
for char in str:
    if char.isupper():
        count=count+1
print("your entered upper case character are=",count)