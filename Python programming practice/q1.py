#write a program that asks the user to enter and odd nuber. 
#program keeps asking h user to ente and odd number till the entered number is odd.

# x=int(input("enter a number:-"))
# while(x%2==0):
#     print("your enter a even number:-",x)

#     x=int(input("enter number again:-"))

#     print("you enter a odd number:",x)

#pattern 01
# y=int(input("enter a number that you want to ask:-"))
# while(y%2==0):
#     print("your enter a even number:-",y)
#     y=int(input("enter a number that you want to ask:-"))

# print("you entered an odd number:-,",y)

#pattern#2
# y=int(input("enter a number that you want to ask:-"))
# while(y%2==0):
#     print("your enter a even number:-",y)
#     y=int(input("enter a number that you want to ask:-"))
# else:
#     print("you entered an odd number:-,",y)




#write a program that asks the user for an integer n and add first n natural number

#logic 1 
# n=int(input("enter an integer:-"))
# sum=0
# for c in range(1,n+1):
#     sum=sum+c
# print(n, "the sum of natural number till:-",sum)

# #logic 2
# n=int(input("enter an integer:-"))
# sum=0
# for c in range(1,n+1):
#     sum=sum+c
# print("the integer is:-",n)
# print("the sum of integer is:-",sum)

# #logic 3
# n=int(input("enter an integer:-"))
# sum=0
# for c in range(1,n+1):
#     sum=sum+c
#     print("the integer is:-",n, "the sum of integer is step by step:-",sum)

#madam agr hum nay sara program check karna hou kesy yei sara process perform ho rha hai to is ka kya 
#procedure ho ga.... kindly explain me....

#by using while looop we can solve this program 

# n=int(input("enter a number:-"))
# sum=0
# i=1
# while(i<=n):
#     sum=sum+i
#     i=i+1
#     print("the integer is:-",n)
#     print("the sum of integer is",sum)


# n=int(input("enter a number:-"))
# sum=0
# i=1
# while(i<=n):
#     sum=sum+i
#     i=i+1
# print("the integer is:-",n)
# print("the sum of integer is",sum)


#write a program that asks the user for an integer n and finds its factorial 

#logic 1 print with in loop
# n=int(input("enter an integer:-"))
# fact=1
# a=1
# while(a<=n):
#     fact=fact*a
#     a=a+1
#     print("the factorial of:",n, "is",fact)

#logic 2 print statement outside loop

# n=int(input("enter an integer:-"))
# fact=1
# b=1
# while(b<=n):
#     fact=fact*b
#     b=b+1
# print("the factorial of: ",n, " is ",fact)


#write a program that asks the user for a number check whether the number is even or odd,
#if the number is even, print its table


#logic 1 (by using 2 variable that user asks)
# n=int(input("enter a number:-"))
# i=int(input("enter your value:-"))
# if(n%2==0):
#     print("this is even number:-",n)
#     for i in range(i,11):
#         print(n, " x ",i, " = ",n*i )
# else:
#     print("you entered an invalid number:-",n)



# #logic 2 
# n=int(input("enter a number:-"))
# if(n%2==0):
#     print("even number:-",n)
#     for i in range(1,11):
#         print(n, " x ",i, " = ",n*i)
# else:
#     print("your entered an invalid number:-",n)


#program can be solved using while loop 

# n=int(input("enter a number:-"))
# if(n%2==0):
#     print("Number is even:-",n)
#     i=1
#     while(i<=10):
#         print(n, " x ",i, " = ",n*i)
#         i=i+1  
# else:
#     print("your entered an invalid number:-",n)

