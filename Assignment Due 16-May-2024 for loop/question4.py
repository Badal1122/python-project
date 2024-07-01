#write a python program that prompts the user to enter a number and prints all the factors of that number
#using a for loop with range

n=int(input("enter a number="))
for i in range(1,n+1):
    if (n%i==0):
        print(i, end=' ')

