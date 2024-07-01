#write a program that asks the user for a number check whether the number is even or odd,
#if the number is even, print its table

#by using for loop to solve the program

#logic 1 (by using 2 variable that user asks)
n=int(input("enter a number:-"))
i=int(input("enter your value:-"))
if(n%2==0):
    print("this is even number:-",n)
    for i in range(i,11):
        print(n, " x ",i, " = ",n*i )
else:
    print("you entered an invalid number:-",n)

#______________________________________________________

# #logic 2 (with declaring a range in loop)

n=int(input("enter a number:-"))
if(n%2==0):
    print("even number:-",n)
    for i in range(1,11):
        print(n, " x ",i, " = ",n*i)
else:
    print("your entered an invalid number:-",n)


#program can be solved using while loop 

n=int(input("enter a number:-"))
if(n%2==0):
    print("Number is even:-",n)
    i=1
    while(i<=10):
        print(n, " x ",i, " = ",n*i)
        i=i+1  
else:
    print("your entered an invalid number:-",n)

