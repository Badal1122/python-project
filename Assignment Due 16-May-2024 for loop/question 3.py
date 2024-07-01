#create a python program that prints the multiplication table of a given number upto 10
#using a for loop with range

#logic 1 (without declaring a variable)

n=5
for i in range(1,11):
    print(n, " x ",i, " = ",n*i)
print("program ended")

#logic 2 (with declaring a variable and the print its table)

n=int(input("enter a number="))
o=int(input("enter your value="))
for o in range(1,o+1):
    print(n, " x ",o, " = ",n*o)