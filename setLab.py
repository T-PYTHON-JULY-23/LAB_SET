nestle_salse ={ "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

unilever_salse ={ "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

#Create a variable to hold the values of Nestle products (use a dicitionary)
nestle_prodcut={
"KitKat" : 34_456_432 ,
"Nescafe" : 14106132,
"Maggi" : 9960312,
"Nido" : 44506003
}

#- Create a variable to hold the values of Unilever_products (Use a dictionary)
unilever_products={ 
    "Lipton" : 23456000,
"Breyers" : 1235891,
"HellManns" : 17241412,
"Marmite" : 11715324}


#- Print each product sold by Unilever and the sales figures / numbers  for that product.
print("\n Unilever product and thire product salse: \n")
for key, value in unilever_products.items():
    print(f"{key}: ${value} ")


#- Print each product sold by Nestle and the sales figures / numbers  for that product.
print("\n Nestle product and thire product salse: \n")
for key, value in nestle_prodcut.items():
    print(f"{key}:$ {value} \n")


#- Print which of the companies has more products that the other company.
if len(nestle_prodcut) > len(unilever_products):
    print("unilever has:")
elif len(unilever_products)>len(nestle_prodcut):
    print(" Nestle has: ")
else: 
    print(" Bothe Nestle and Unilever have the same number of products.. ")


#- Print the top selling product from Nestle with sales figures.
nestle_top_selling_product_figur=0
nestle_top_selling_product_key= ""
for key, v in nestle_prodcut.items():
    if v> nestle_top_selling_product_figur:
        nestle_top_selling_product_figur=v
        nestle_top_selling_product_key=key

print(f"Top selling product in Nestle is: {nestle_top_selling_product_key} with ${nestle_top_selling_product_figur} ")

#- Print the top selling product from Unilever with sales figures.
unilever_top_selling_product_figur=0
unilever_top_selling_product_key= ""
for key, v in unilever_products.items():
    if v> unilever_top_selling_product_figur:
        unilever_top_selling_product_figur=v
        unilever_top_selling_product_key=key


print(f"Top selling product in Unilever is: {unilever_top_selling_product_key} with ${unilever_top_selling_product_figur} ")

#- Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print("\n the cities Unilever & Nestle sell their products in is: \n ")

unilever_nestle_sell = nestle_salse | unilever_salse  
for country in enumerate(unilever_nestle_sell, start=1):
    print(country)


#- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("\n Cities that both Nestle & Unilver sell in is:") 

nestle_unilver_country=nestle_salse.intersection(unilever_salse)
for country in enumerate(nestle_unilver_country, start=1):
    print (country)

#- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print("\n Cities Nestle sells in , but Unilver doens't sell in: ") 
not_in_unilver=nestle_salse.difference(unilever_salse)
for country in enumerate(not_in_unilver, start=1):
    print (country)