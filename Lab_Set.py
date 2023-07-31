nestle_products={"KitKat" : 34456432,
"Nescafe" : 14106132 ,
"Maggi" : 9960312 ,
"Nido" : 44506003 }

unilever_products={"Lipton" : 23456000 ,
"Breyers" : 1235891 ,
"HellManns" : 17241412 ,
"Marmite" : 11715324 }


# Print each product sold by Unilever and the sales figures / numbers for that product
print("Unilever products:")
for product, sales in unilever_products.items():
    print(product, ":", sales, "US Dollars")

# Print each product sold by Nestle and the sales figures / numbers for that product
print("Nestle products:")
for product, sales in nestle_products.items():
    print(product, ":", sales, "US Dollars")

# Print which of the companies has more products that the other company
if len(nestle_products) > len(unilever_products):
    print("Nestle has more products than Unilever.")
else:
    print("Unilever has more products than Nestle.")

# Print the top selling product from Nestle with sales figures
top_nestle_product = max(nestle_products, key=nestle_products.get)
top_nestle_sales = nestle_products[top_nestle_product]
print("Top selling Nestle product:", top_nestle_product, "with", top_nestle_sales, "US Dollars")

# Print the top selling product from Unilever with sales figures
top_unilever_product = max(unilever_products, key=unilever_products.get)
top_unilever_sales = unilever_products[top_unilever_product]
print("Top selling Unilever product:", top_unilever_product, "with", top_unilever_sales, "US Dollars")

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in
nestle_cities = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_cities = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print("Cities where Nestle sells products:")
for city in nestle_cities:
    print(city)

print("Cities where Unilever sells products:")
for city in unilever_cities:
    print(city)

# Using Sets & a loop, print the cities that both Nestle & Unilever sell in common
common_cities = nestle_cities.intersection(unilever_cities)
print("Cities where both Nestle and Unilever sell products:")
for city in common_cities:
    print(city)

# Using Sets & a loop, print the cities Nestle sells in, but Unilever doesn't sell in
nestle_only_cities = nestle_cities.difference(unilever_cities)
print("Cities where only Nestle sells products:")
for city in nestle_only_cities:
    print(city)
