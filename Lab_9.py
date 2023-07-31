
#Create a variable to hold the values of Nestle products (use a dicitionary)
Nestle_products ={"KitKat" : 34456432 ,"Nescafe" : 14106132 ,"Maggi" : 9960312 ,"Nido" : 44506003 }
#Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever_products ={"Lipton" : 23456000 ,"Breyers" : 1235891 ,"HellManns" : 17241412 ,"Marmite" : 11715324 }

Nestle_country={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_country={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

#Print each product sold by Unilever and the sales figures / numbers for that product.
print(Nestle_products)
#Print each product sold by Nestle and the sales figures / numbers for that product.
print(Unilever_products)
#Print which of the companies has more products that the other company.
if len(Nestle_products)>len(Unilever_products):
    print("Nestle have more prodects than Unilever ")
elif len(Nestle_products)<len(Unilever_products):
    print(" Unilever have more prodects than Nestle ")
else:
    print ("there have the same amout of prodects")


#Print the top selling product from Nestle with sales figures.
print(f"the top selling product from Nestle is  {max(Nestle_products.keys())} :{max(Nestle_products.values())} US Dollars")
#Print the top selling product from Unilever with sales figures.
print(f"the top selling product from Unilever is  {max(Unilever_products.keys())} :{max(Unilever_products.values())} US Dollars")
#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print("cities Unilever & Nestle sell their products in")
for country in Nestle_country & Unilever_country:
    print(country)
#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("cities that both Nestle & Unilver sell in common")
for country in Nestle_country | Unilever_country:
    print(country)
#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print("cities Nestle sells in , but Unilver doens't sell in.")
for country in Nestle_country - Unilever_country:
    print(country)



