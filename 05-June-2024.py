#Question NO:2
# Write a function that greets a user, where the name is a required parameter,
# and the greeting message and punctuation are optional parameters with default values.

#Question No: 2 by using logic 1

def greet_user(name,greeting_message='kya hal hai',punctuation='@'):
    return (name,greeting_message,punctuation)
print(greet_user('Talha'))
print('hello')

#logic 2 by using return function with f variable

def greet_user(name, greeting_message='kya hal hai', punctuation='@'):
    return f"{name}, {greeting_message}{punctuation}"

print(greet_user('Talha'))

