# def greet(): #declaring simple greet function 
#     print("welcome to Knowledge stream")
#     print("hello world")
# greet()

# #difference between parameter and arguments
# #the parameter is the input that you define for your function whereas argument is the actual value 
# # of given parameter

# #FUNCTION WTIH FIRST NAME AND LAST NAME...

# def greet(first_name,last_name):
#     # return first_name,last_name
#     print (f"{first_name},{last_name}")
# print("Adil ", "sial")


# #in Programming we have two types of function 
# #that perform a task
# #return a value 

# def get_greet(name):
#     return name
# print(get_greet("Welcome to knowledge stream"))



# def multiply(a,b):
#     return a*b
# print(4*5)



# def multiply(*numbers):
#     # return numbers
#     multiply=1
#     for i in numbers:
#         multiply=multiply*i
#     return multiply
    

# print(multiply(2,5,10,20))



#types of arguments 
#default arguments
#positional argumensts
#keyword arguments
#arbitray positional arguments
#arbitary keyword arguments


# def greet(name,dept,city):
#     return f"Hi {name},{dept},{city}"
#     # return (f"are you from {dept} department")
#     # return f"you are from{city}"

# print(greet("Adil","CS","lahore"))



def fizz_buzz(input):
    if input % 3==0 and input % 5 ==0:
        return "FizzBuzz"
    if input % 3==0:
        return "Fizz"
    if input % 5==0:
        return "Buzz"
    return input
print(fizz_buzz(10))