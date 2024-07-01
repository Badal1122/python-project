# Design a function that performs arithmetic operations (addition, subtraction, multiplication, division) 
# based on two required numbers and an optional operation parameter with a default value of addition.

def arithmetic_operation(a,b,operator):
    if operator =="+":
        return a+b
    elif operator =="-":
        return a-b
    elif operator =="*":
        return a*b
    elif operator =="/":
        return a/b
    else:
        return "invailid operator"
print(arithmetic_operation(10,2,"+"))


     

