#write a program that asks the user for an integer n and add first n natural number

#logic 1 
n=int(input("enter an integer:-"))
sum=0
for c in range(1,n+1):
    sum=sum+c
print(n, "the sum of natural number till:-",sum)

#------------------------------------------------------------------

# #logic 2
n=int(input("enter an integer:-"))
sum=0
for c in range(1,n+1):
    sum=sum+c
print("the integer is:-",n)
print("the sum of integer is:-",sum)

#__________________________________________________________

# #logic 3
n=int(input("enter an integer:-"))
sum=0
for c in range(1,n+1):
    sum=sum+c
    print("the integer is:-",n, "the sum of integer is step by step:-",sum)

#madam agr hum nay sara program check karna hou kesy yei sara process perform ho rha hai to is ka kya 
#procedure ho ga.... kindly explain me....

#_____________________________________________________________________




#by using while looop we can solve this program 



#logic 1
n=int(input("enter a number:-"))
sum=0
i=1
while(i<=n):
    sum=sum+i
    i=i+1
    print("the integer is:-",n)
    print("the sum of integer is",sum)
#___________________________________________________________



#logic 2
n=int(input("enter a number:-"))
sum=0
i=1
while(i<=n):
    sum=sum+i
    i=i+1
print("the integer is:-",n)
print("the sum of integer is",sum)
