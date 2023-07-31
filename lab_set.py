# Create a variable to hold the values of Nestle products (use a dicitionary)
Nestle_products = {
    "34,456,432 US Dollars": "KitKat",
    "14,106,132 US Dollars" : "Nescafe",
    " 9,960,312 US Dollars" : "Maggi",
     "44,506,003 US Dollars" : "Nido"

}

#- Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever_products = {
    "23,456,000 US Dollars" : "Lipton" , 
    "1,235,891 US Dollars" : "Breyers",
    "17,241,412 US Dollars" : "HellManns",
    "11,715,324 US Dollars" : "Marmite"
}



#Print each product sold by Unilever and the sales figures / numbers  for that product.
for key, value in Unilever_products.items():
    print( key , ": ", value) 
print("-"*30)

#Print each product sold by Nestle and the sales figures / numbers  for that product.
for key, value in Nestle_products.items():
    print( key , ": ", value) 
print("-"*30)




# Print which of the companies has more products that the other company.
if len(Nestle_products) > len(Unilever_products):
    print("the Nestle products is more than Unilever products ")
elif len(Unilever_products) < len(Nestle_products):
    print("the Unilever products is more than Nestle products")
else:
    print("the product of the company is the same")
print("-"*30)




#Print the top selling product from Nestle with sales figures.
# Print the top selling product from Unilever with sales figures.
max_value1 = max(Nestle_products)
print(f"top selling product from Nestle: {max_value1}")

max_value2 = max(Unilever_products)
print(f"top selling product from Unilever: {max_value2}")
print("-"*30)





#- Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
set_cities_nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
set_cities_unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

cities_union = set_cities_nestle.union(set_cities_unilever)
print("cities Unilever & Nestle sell their products in: " )

for city_un in cities_union :
    print(city_un)
print("-"*30)





#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
cities_intersaction = set_cities_nestle.intersection(set_cities_unilever)
print("cities that both Nestle & Unilver both in: ")
for city_in in cities_intersaction:
    print(city_in)






print("-"*30)
#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
cities_difference = set_cities_nestle.difference(set_cities_unilever)
print(" the cities Nestle sells in , but Unilver doens't sell in: ")
for ciry_di in cities_difference:
    print(ciry_di)