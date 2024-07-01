# Create a function create_user that takes a mandatory username argument and any number
# of keyword arguments with default values for email (None), password (None), and
#  is_admin (False). The function should print the created user details,
#  including the username and any provided or default values for email, password, and is_admin.

def create_user(**kwargs):
    print("User details\n")
    for key,value in kwargs.items():
        print(key,value)

create_user(username="adilsial05",num="03045258372",email=None,password=None,is_admin=False,)
