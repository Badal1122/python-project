#develop a python program that calculates the sum of all the postive integers less than 100 that are not 
#divisible by 5. using the continue statement to skip number divisible by 5


#logic (with checking step by step program how to add sum of the numbers)

# num=0
# sum=0
# while(num<100):
#     if(num%5==0):
#         num=num+1
#         continue
#     print(num, end= ' ')
#     sum=sum+num
#     num=num+1
# print("\nthe sum is=",sum)



# #logic 2 (without checking step by step program)


# num=0
# sum=0
# while(num<100):
#     if(num%5==0):
#         num=num+1
#         continue
#     print(num, end= ' ')
#     sum=sum+num
#     num=num+1
# print("\nthe sum is=",sum)



num=0
sum=0
while(num<100):
    if(num%5==0):
        num=num+1
        continue
    num=num+1
    print(num, end=' ')
    sum=sum+num
print("\nthe sum is=",sum)
