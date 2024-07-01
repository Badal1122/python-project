#write a python program that print all the odd number from 1 to 10, skipping even number using the continue 
#statement......

num=1
while(num<=10):
    if(num%2==0):
        num+=1
        continue
    print(num)
    num+=1
