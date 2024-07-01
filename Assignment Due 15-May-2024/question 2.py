#create a python program that simulates a password guessing game. the program should promot the user 
#to enter a password and keep asking untill the correct password is entered or the user enter "quit"
#using the break statement to exit the loop when the correct password is entered... 

#logic 1(program exit when user enter correct password but nothing to show in terminal)


password="12345"
x=input("enter your password=")
while(x!=password):
    x=input("ented your passowrd again=")
    if(x==password):
        break
    print("your enterd correct password=",x)


#logic

password="12345"
x=input("enter your password=")
while(x!=password):
    x=input("ented your passowrd again=")
    if(x==password):
        break
    print("your enterd correct password=",x)
