# How can you create a function that generates a user profile with required parameters for name and age,
#  and optional keyword parameters for additional information like location and occupation?

def user_profile(name="Adil",age="23",location="Lahore",occupation="Python Learner"):
    return f"{name}, {age}, {location}, {occupation}"
print(user_profile('Adil',24))