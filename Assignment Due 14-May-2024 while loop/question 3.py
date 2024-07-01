#write a program that asks the user for an integer n and finds its factorial 

#logic 1 print with in loop (factorial shows step by step )


n=int(input("enter an integer:-"))
fact=1
a=1
while(a<=n):
    fact=fact*a
    a=a+1
    print("the factorial of:",n, "is",fact)
#_______________________________________________________________

#logic 2 print statement outside loop (factorial direct show)

n=int(input("enter an integer:-"))
fact=1
b=1
while(b<=n):
    fact=fact*b
    b=b+1
print("the factorial of: ",n, " is ",fact)

#______________________________________________-