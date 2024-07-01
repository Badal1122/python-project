#using an if-else python program that take total number of electricity units from user and caluclate total 
#electricity bill according to the given condition:
#For the first 50 units Rs. 15/unit
#For the next 100 units Rs. 20/unit
#For the next 100 units Rs. 30/unit
#For unit above 250 Rs. 50/Unit 
#An additional surcharge of 20% is added to the bill 

#using simple if elif statement

# nou=int(input("enter total number of units:-"))
# if(nou<=50):
#     bill_amount=nou*15
# elif(nou<=150):
#     bill_amount=(50*15)+(nou-50)*20
# elif(nou<=250):
#     bill_amount=(50*15)+(100*20)+(nou-150)*30
# else:
#     bill_amount=(50*15)+(100*20)+(100*30)+(nou-250)*50
# print("bill amount is:-",bill_amount)
# surchrge=bill_amount*0.20
# print("Surcharge is:-",surchrge)
# TEBill=bill_amount+surchrge
# print("total Electricity bill is:-",TEBill)
# print("program Ended")






# by using logical operator we can solve this program 
# nou=int(input("enter total number of units:-"))
# if(nou<=50 or nou>0):
#     bill_amount=nou*15
# elif(nou<=150 or nou>50):
#     bill_amount=(50*15)+(nou-50)*20
# elif(nou<=250 or nou>150):
#     bill_amount=(50*15)+(100*20)+(nou-150)*30
# else:
#     bill_amount=(50*15)+(100*20)+(100*30)+(nou-250)*50
# print("bill amount is:-",bill_amount)
# surchrge=bill_amount*0.20
# print("Surcharge is:-",surchrge)
# TEBill=bill_amount+surchrge
# print("total Electricity bill is:-",TEBill)
# print("program Ended")



#write a python program that takes the qunatity of a product purchased by a customer as input and calculates 
#the total bill amount according to the following conditions:
#For Quantities less than or equal to 10, the cost per unit is Rs. 100.
#For Qunatities greater than 10 and less than or equal to 20, the cost per unit is RS. 90
#For Quantities greater than 20 and less than or equal to 30, the cost per unit is RS. 80
#For Quantites above 30, the cost per unit is RS. 70
#Additionaly, apply a discount of 10% on the total bill amount.....


prod=int(input("Takes the qunatity of product:-"))
if(prod<=10):
    cost=prod*100
elif(prod>10 and prod<=20):
    cost=prod*90
elif(prod>20 and prod<=30):
    cost=prod*80
else:
    cost=prod*70
print("Quanities cost:-",cost)
disc=cost*0.1
print("Discount of Product:-",disc)
bill_amount=cost-disc
print("Total Bill amount is:-",bill_amount)

