
# Write a Python program that takes a password and tell whether password is strong or weak.
# If password is weak, keep taking password again and again till password is strong.
# A strong password is at least 8 characters long, contains both uppercase and lowercase letters,
# and includes at least one digit. Use loops and conditionals to check password.



while True:
    password=input("enter you password=")

    if(len(password)<8):
        print("password should be at least 8 characters")
        continue
    if(len(password)>20):
        print("password should between 8 and 20 characters")
        continue
    # if(password.isdigit()==True):
    #     print("password should be upper and lowercase")
    #     continue
    if(password.islower()==True or password.isupper()==True or password.isdigit()==True):
        print("password is weak")
        continue
    else:
        (password.islower()==True and password.isupper()==True and password.isdigit()==True)
        print("your password is strong=",password)
    break



