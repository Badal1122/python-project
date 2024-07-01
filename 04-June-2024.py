

def Average(*a):
  # calculate the sum of all values
  # find the average by dividing the sum with the count of values
  # return average

#logic 1 by using arbitray arguments without declaring a tuple

  sum=0
  for i in a:
    sum=sum+i
  print(sum)
  avg=sum/len(a)
  return avg
print(Average(1,5,6,8))

# calculate the sum of all values
  # find the average by dividing the sum with the count of values
  # return average
#logic 2 by using arbitray arguments with declaring a tuple 

def Avg(*c): 
    sum=0
    # c=(1,5,8,9,10,25,30,45)
    for i in c:
      sum=sum+i
    print("the sum of all values is=",sum)
    avge=sum/len(c)
    return avge
print("the Avergae is=",Avg(1,2,3,45,50,51))
  







def Factorial(num):
  # calculate the factorial of the given number using loop
  # return the factorial
  # if the passed value is not integer return None


    f=1
    for i in range(1,num+1):
        f=f*i
    return f
num=int(input("enter your factorial number="))
print("the Factorial is",Factorial(num))


#write a function that takes two numbers and return their sum

#logic 1 without taking input number from user

def sum(a,b):
    sum=a+b
    return sum
print("The sum of two number is=",sum(45,568))


#logic 2 taking input number from user and return their sum

def sum(n1,n2):
    sum=n1+n2
    return sum
n1=int(input("enter your first number="))
n2=int(input("enter your second number="))
print(sum(n1,n2))
print(sum(n1,n2))



#Question No:2
#Write a function that takes three numbers and return the maximum

#logic 1 by using print function 

def Maximum_num(a,b,c):
    if a>b and a>c:
        print("the maximum number is",a)
        # return a
    elif b>a and b>c:
        print("the maximum number is",b)
        # return b
    else:
        print("the maximum number is",c)
        # return c
print(Maximum_num(45,43,36))


#logic 2 by using retrun function

def Maximum_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print("the Maximum number is=",Maximum_num(45,43,36))



#write a program to calculate a factorial of given number

#logic 1 by taking input number from user to calculate the Factorial 

def Factorial(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f
num=int(input("Enter your Factorial number="))
print("the Factorial of given number is",Factorial(num))

#logic 2 without taking input number from user to calculate the factorial 


def Factorial(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f
print("the Factorial of that number is=",Factorial(8))



#Question NO:4 
#Write a fuction to check if a given string is palindrome....


def isPalindrome(str):
    if str==str[::-1]:
        return True
    else:
        return False
print(isPalindrome("cat"))



def reverse(x):
  return x[::-1]

mytxt = "I wonder how this text looks like backwards"

print(reverse(mytxt))


#Write a function that counts the number of vowels in a given string

def count_vowels(ctr):
    count=0
    vowels="AEIOUaeiou"
    for i in ctr:
        if i in vowels:
            count=count+1
    return count
print(count_vowels("I love coding but i do not know how can we handle the problem solving")) 

#Write a function to flatten a nested list #this is my favorite question 



def flat_list(mylist):
    hello=sum(mylist, [])
    return hello
mylist=[[1],[2,3],[5,6,7]]
print(flat_list(mylist))

  

