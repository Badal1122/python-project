# str=input("enter a string")
# x=str.split('@')
# print(x)
# domain="gmail.com"
# for i in x:
#     if i==domain:
#         print(domain)


# str=input("enter a gmail=")
# x=str.split('@')
# if len(x)>2:
#     print(x)
# else:
#     print(x[-1])


# yei_cheex=input("enter your line")
# vowels="aeiouAEIOU"
# vowel_count=0
# for i in yei_cheex:
#     if i in vowels:
#         vowel_count+=1
# print("your total vowel is=",vowel_count)


# Never_giveup="sdfs,dlf,sjs,dlfj,sdfsdf,sdlfjs,lfjs,df"
# x=Never_giveup.split(',')
# long=""
# for i in x:
#     if len(i)>len(long):
#         long=i
#     print(long)
# else:
#     print(x)





str=input("enter a gmail=")
x=str.split('@')
if (len(x)>2):
    print(x)
else:
    print(x[-1])