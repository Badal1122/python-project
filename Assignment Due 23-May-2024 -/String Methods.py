#python String Methods 




#1- Python string Capitalize
#The captalize method converts the first character of a string to an upper case letter and all 
#other to lower case letters...
#Capatilze() syntax
#the syntax of capitalize method is 
#string.capitalize()


str="welcome To Knowledge stream."
x=str.capitalize()     #Capitalize method does not change the original string...
print(x)


#2- python String Center
#The centre method returns a new centered string after padding id with the specified character..
#Center() syntax
#The syntax of Center method is 
#string.center(width,'fillchar')

str="I love pakistan"
x=str.center(50,'*')
print(x)



#3- Python casefold method
# the casefold method converts all the character of the string into lowercase letters and retruns a
# new String 
# The syntax of Casefold method is 
# str.casefold()

str="CONVERT ALL THE CHARACTERS INTO LOWER CASE LETTERS"
y=str.casefold()
print(y)


#4- python string count
#The count method returns the number of occurrrences of a substring in a given string
#the syntax of string count is 
#str.count(substring,strat=....,end=....) (substring whose count is to be found)


str="returns the number of occurrences of a substring in a given string"
z=str.count('r',0,7)
print(z)



#5- Python string endswith
#the endswith method returns true if a string ends with the specified suffix. if not it return false
#the syntax of string endswith is
#  string.endswith('suffix',start and endig index is optional)

# str="Knowledge is best platform for learning"
# print(str.endswith('ing'))

# 6- Python String Find
# The find() method returns the index of first occurrence of the substring (if found). 
# If not found, it returns -1.
# the syntax of string find is 
# string.find('sub',start and ending point)


str='I Love pakistan'
print(str.find('tan'))


# 7- Python string index 
# the method returns the index of a substring inside a string (if found). if the substring is not Found
# it raise an Exception
#the syntax of string index is 
#string.index(sub, start and ending valuse)

str="Hi how are you"
print(str.index('how'))


# 8- python string isalnum
# the method returns true if all the characters in given string is alpahnumeric(either alpahabet)
# either it returns falsenjm
#the syntax of string 
#string.isalnum()

str="Adilsial787"
print(str.isalnum())


# 9- python string isalpha
# the method returns true if all the characters in string is alpha(both upper and lower case)
# False if at least one character is not alpahabet 
# the syntax of string alpha 
# string.isaplha()


str="Knowledge stream is best"
print(str.isalpha())


# 10- Python string isdecimal
# the method returns true if all characters in string are decimal character. 
# False if atleast one character is not decimal
# the syntax of string isdecimal is 
# string.isdecimal() 

str="123345646s"
print(str.isdecimal())


# 11- python string isdigit
# True if all characters in string are digit if not it returns false
# the syntax of string isdigit is
# string.isdigit()

str="12313131"
str1="sfsfsf2122"
print(str.isdigit())
print(str1.isdigit())


# 12- python string isidentifier
# True if a string is a valid identifer
# False if a string is not a invalid identifer
# the syntax of string isdentifer
# string.isidentifer()

str="Python"
str2="P thon "
print(str.isidentifier())
print(str2.isidentifier())



# #13- python String islower
# True if all the characters in a string is lowercase
# False if at least one character is upper case 
# the syntax of string islower is 
# string.islower()


str="adilsial"
str1="Adilsial"
print(str.islower())
print(str1.islower())


#14- python string isnumeric
#true if all the characters in a string is numeric
#False if at least one character is not numeric
# the syntax of string isnumeric is 
# stirng.isnumeric()


str="6469494"
str2="2131313d"

print(str.isnumeric())
print(str2.isnumeric())



# #15- python string isprintable
# True if all the characters in a string is printable
# False if at least one character is non-printable
# the syntax of string isprintable is 
# string.isprintable()

str="python"
str4="python\n"
print(str.isprintable())
print(str4.isprintable())


# 16-python string isspace
# true if all characters in a string are whitespace characters
# (charcters that are used for spacing are called white space characters. etc tab, space, newline)
# false if string is empty, or at least one in non-printable character 
# the syntax of string isspace is
# string.isspace()

str=" "
str1=""
print(str.isspace())
print(str1.isspace())


# 17- python string istitle
# true if the string is title case string
# False if string is empty or not titlc case string
# the syntax of string istitle is 
# string.istitle()


str="This Ss A Program"
str2="2 is a program"
print(str.istitle())
print(str2.istitle())


# 18- python string isupper
# true if all characters in a string is uppeercase
# false if at least one character is lowercase
# the syntax of string isupper is 
# string.isupper()

str="THIS IS A PROGRAM"
str2="thi IS a program"
print(str.isupper())
print(str2.isupper())



# 19-pyhton String lower
# the method converts all the uppercase characters in a string into lowercase and returns it.
# the syntax of string lower is 
# string.lower()

str="THIS IS A Program"
print(str.lower())

# 20- python string uppper 
# the method converts all the lowercase characters in a string into uppercase and retruns it. 
# the syntax of string upper is 
# string.upper()


str="knowledge stream"
print(str.upper())

# 21- python string swapcase
# the method converts all the characters to their opposite case letter (upper to lower and vice versa)
# the syntax of string swapcase is 
# string.swapcase()


str="KNOW stream"
print(str.swapcase())



# 22-python string replace
# the method replaces each matching occurences of a substring with another String
# the syntax of string replace is 
# string.replace()

str="matching occurences of a substring with another string"
print(str.replace('mat', 'not'))


# 23-python string startswith
# true if a string start with a specified characters. if not it returns false
# the syntax of string startswith is 
# string.startswith(prefix, starting and ending value)


str="this is a program"
print(str.startswith('this'))
print(str.startswith('is', 4,15))


# 24- python string title
# method returns a title case version of a string. meaning the first charcter of each word is capitalized
# the syntax of string title is 
# string.title()

str="i want to become a data scientist"
print(str.title())
