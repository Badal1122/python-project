#develop a python program that calculates the sum of all the integers from 1 to 50. 
#using a for loop with range


#logic 1 (without declaring a variable)
sum=0
for i in range(1,51):
    sum=sum+i
print("Sum of all integer is=",sum)


#logic 2 (with print all integers which we want to sum)

sum=0
for i in range(1,51):
    print(i, end=' ')
    sum=sum+i
print("sum of all integer is=",sum)


#logic 3 (with declaring a variable and print sum of all integer outside loop)

n=int(input("enter a number="))
sum=0
for i in range(1,n+1):
    print(i, end=' ')
    sum=sum+i
print("sum of all integer is=",sum)


#logic 4 (with declaring a variable and print sum within loop)

n=int(input("enter an integer="))
sum=0
for i in range (1,n+1):
    print(i,end=' ')
    sum=sum+i
    print(sum)
