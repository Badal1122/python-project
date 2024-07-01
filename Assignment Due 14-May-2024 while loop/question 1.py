#question 1
#write a program that asks the user to enter and odd nuber. 
#program keeps asking h user to ente and odd number till the entered number is odd.

y=int(input("enter a number that you want to ask:-"))
while(y%2==0):
    print("your enter a even number:-",y)
    y=int(input("enter a number that you want to ask:-"))

print("you entered an odd number:-,",y)

print("program Ended")