# write a program that asks the user to enter an interger and update ii into its upper neartest odd number 
#if the entered nmber is even

# x=int(input("enter an Integer:-"))
# if(x%2==0):
#     print("upper nearest odd number",x+1)
# else:
#     print("Upper nearest number is not odd")
# print("Program Ended")

    
#using an if-else python program to take a value form the user as input marks of five subjects Physics, 
#Chemistry, Biology, Mathematics, and computer, Calculate percentage and grade 
#According to the Following
#Percentage >=90%: Grade A
#Percentage >=80%: Grade B
#Percentage >=70%: Grade C
#Percentage >=60%: Grade D
#Percentage >=40%: Grade E
#Percentage <40% : Grade F

phy=int(input("Enter marks of Physics:-"))
che=int(input("Enter marks of Chemistry:-"))
bio=int(input("Enter marks of Biology:-"))
Math=int(input("Enter marks of Math:-"))
Comp=int(input("Enter marks of Computer:-"))
Per=(phy+che+bio+Math+Comp)/5
print("Percentage is:-",Per)
if(Per>=90):
    print("Grade A")
elif(Per>=80):
    print("Grade B")
elif(Per>=70):
    print("Grade C")
elif(Per>=60):
    print("Grade D")
elif(Per>=40):
    print("Grade E")
else:
    print("Grade F")
print("Program Ended")


#write a python program that takes two integers as iput and determines whether the first integer is divisible
#by the second integer wihout leaving a remainder. print the result accordingly...


# x=int(input("enter 1st inter:-"))
# y=int(input("enter 2nd integer:-"))


# if(x%y==0):
#     print("Remainder is zero")
# else:
#     print("remainder is not zero")
# print("program Ended")


#write a python program that prompts the user to input their age and checks if they are eligible to vote. 
#Assume the legal voting age is 18. Print"Eliglibe" if the age is 18 or above, otherwise print "Not eligible"


# age=int(input("enter your age:-"))
# if(age>=18):
#     print("Eligible")
# else:
#     print("Not Eligible")
# print("program Ended")

#write a python program that checks whether a specified character entered by user is present in a given
#string. Provide the code snippet using appropriate conditional statements.

# x="Tell me about yourself with in 2 minutes"
# y=input("check a specifies character:-")
# if(y in x):
#     print("y found in x")
# else:
#     print("y not found in x") #1 sequence say search karta hai......
# print("Program Ended")




#write a program that inputs temperature and display a message according to the follwoing data...
#temperature>35 Hot Day
#temperature<35 pleasent day
#temperature<25 Cool day


# temp=int(input("Enter you temperature:-"))
# if(temp>35):
#     print("Hot Day")
# elif(temp>25):
#     print("Pleasent Day")
# else:
#     print("cool day")
# print("program ended")



