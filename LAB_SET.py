'''
Create a variable to hold the values of Nestle products (use a dicitionary)
Create a variable to hold the values of Unilever products (Use a dictionary)
Print each product sold by Unilever and the sales figures / numbers for that product.
Print each product sold by Nestle and the sales figures / numbers for that product.
Print which of the companies has more products that the other company.
Print the top selling product from Nestle with sales figures.
Print the top selling product from Unilever with sales figures.
Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.

'''
Nestle_products  = {
"KitKat" : 34456432,
"Nescafe" : 14106132,
"Maggi" : 9960312,
"Nido" : 44506003
}

Unilever_products = {
    "Lipton" : 23456000,
"Breyers" : 1235891,
"HellManns" : 17241412,
"Marmite" : 11715324
}
print("*"*25)
print()
for key,value in Nestle_products.items():
    print(f"{key} : {value} US")
print()
for key,value in Unilever_products.items():
    print(f"{key} : {value} US")
avg_Nestle:int = [Nestle_value for Nestle_value in Nestle_products.values()]
print("The average of the price Nestle products is :",sum(avg_Nestle)/len(avg_Nestle))

avg_Unilever:int = [Unilever_value for Unilever_value in Unilever_products.values()]
print("The average of the price Unilever products is :",sum(avg_Unilever)/len(avg_Unilever))
if len(avg_Unilever) > len(avg_Nestle) :
    print("The prodcuts of  Unilever is greater than Nestle")
else:
    print("The prodcuts of  Nestle is greater than Unilever")
print("*"*3)
# Print the top selling product from Nestle with sales figures.
print(f"the top selling product from Nestle :{max(Nestle_products)}")
# Print the top selling product from Unilever with sales figures.
print(f"the top selling product from Unilever :{max(Unilever_products)}")




# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
Nestle_Unilever_union = Nestle | Unilever
for i in Nestle_Unilever_union:
    print(i, end=" ")
print()
Nestle_Unilever_intersection = Nestle & Unilever
for i in Nestle_Unilever_intersection:
    print(i,end=" ")
print
Nestle_Unilever_difference = Nestle - Unilever
for i in Nestle_Unilever_difference:
    print(i,end=" ")