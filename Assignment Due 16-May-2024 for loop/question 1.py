#write a program that prints all the even number from 1 to 20 using a for loop with range

#logic 1 (without declaring a variable)

for i in range(1,21):
    if (i%2==0):
        print(i)


#logic 2(with declaring a variable)

n=int(input("enter a number"))
for i in range(1,n+1):
    if (i%2==0):
        print(i, end=' ')
print("program ended")