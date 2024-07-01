
#develop a python program that calculates the total cost of a grocery purchase based on the selected items 
#and the quantity purchased. The program should prompt the user to input the item names and quantities 
#Apples cost $1 per pound
#Bananas cost 0.50 per pound
#oranges cost 0.75 per pound
#Additional apply a 5% discount on the total bill if the total purchase amount exceeds $50.

item_name=input("enter the item name:-")
quan=int(input("enter the quantity value:-"))
if(item_name=='apple'):
    price_perunit=1
    cost=price_perunit*quan
    print("your apple cost is:-",cost)
elif(item_name=='banana'):
    price_perunit=0.5
    cost=price_perunit*quan
    print("your banana cost is:-",cost)
elif(item_name=='orange'):
    price_perunit=0.75
    cost=price_perunit*quan
    print("your orange cost is:-",cost)
else:
    print("you enterd an invalid item")


if(cost>50):
    discount=cost*0.05
    print("discount is:-",discount)
    total_cost=cost-discount
    print("total cost is:-",total_cost)
else:
    print(cost)
print("program ended")


#question no 2 is solved but i am not sure about that it is true or false,tommorow madam will check out that 
#question then every thing is clear about.

# dish_choice=input("enter your dish choice:-")
# time=input("enter the time:-")
# if(dish_choice=="maincourse" and time.lower()=="lunch"):
#     price=15
#     discout=price*0.1
#     print("discount of maincourse is:-",discout)
#     total_cost=price-discout
#     print("total cost is:-",total_cost)
# elif(dish_choice=="appetizer" and time.lower()=="lunch"):
#     price=8
#     print("price of dish is:-",price)
#     discount=price*0.1
#     print("discount price of appetizer is:-",discount)
#     total_cost=price-discount
#     print("total cost of appetizer is:-",total_cost)
# elif(dish_choice=="dessert" and time.lower()=="lunch"):
#     price=6
#     discount=price*0.1
#     print("discount of dessert is:-",discount)
#     total_cost=price-discount
#     print("total cost of dessert is:-",total_cost)
# else:
#     print("your entered and invalid dish choice and time is not lunch time")

# print("program ended")
    
