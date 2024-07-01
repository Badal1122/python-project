# Write a Python program that prompts the user to enter a series of numbers
# and stops taking input when the user enters a negative number, using the break statement.

#logic 1(nothing to show after break statement when you print the statement in loop)


num=0
while(num!=-1):
    num=int(input("enter a number="))
    if(num<0):
        break
    print("program ended and the number is negative=",num)
#_______________________________________________________________    



#logic 2(show statement after break statment when you print outside of your loop)



num=0
while(num!=-1):
    num=int(input("enter a number="))
    if(num==-1):
        break
print("your entered a negative number=",num)

#__________________________________________________________________