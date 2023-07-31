# Create a variable to hold the values of Nestle products (use a dicitionary)
Nestle_products ={"KitKat": 34456432,
                  "Nescafe": 14106132,
                  "Maggi":9960312,
                  "Nido": 44506003
                  }
#Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever_products ={"Lipton":23456000,
                    "Breyers":1235891,
                    "HellManns":17241412,
                    "Marmite": 11715324
                    }

#- Print each product sold by Nestle and the sales figures / numbers  for that product.
print("\n--- product sold by Nestle--\n")
for key,value in Nestle_products.items():
    print(f"product is: {key} - sales figures: {value} $")

#Print each product sold by Unilever and the sales figures / numbers  for that product.
print("\n--- product sold by Unilever--\n")
for key,value in Unilever_products.items():
    print(f"product is: {key} - sales figures: {value} $")

# Print which of the companies has more products that the other company.
print("\n\n")
if len(Nestle_products)>len(Unilever_products):
   print("Nestle company have more prodect ")
elif  len(Nestle_products)<len(Unilever_products):
    print("Unilever company have more prodect ")
else:
    print("Nestle and Unilever have the same number of product")
    
print("\n\n")


#- Print the top selling product from Nestle with sales figures.

top_selling=max(Nestle_products.values())
top_prodect= {prod for prod in Nestle_products if Nestle_products[prod]==top_selling}

print(f"the top selling product from Nestle is :{top_prodect} {top_selling} $")
print("\n\n")


#Print the top selling product from Unilever with sales figures.
top_selling_Unilever=max(Unilever_products.values())
top_prodect_Unilever= {prod for prod in Unilever_products if Unilever_products[prod]==top_selling_Unilever}

print(f"the top selling product from Unilever is :{top_prodect_Unilever} {top_selling_Unilever} $")
print("\n\n")


# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
Nestle ={ "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever= { "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
union=Nestle.union(Unilever) 
print(f"all the cities Unilever & Nestle sell their products in:")
for city in union:
    print(city)
print("\n\n")

#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
commen=Nestle.intersection(Unilever) 
print(f"cities that both Nestle & Unilver sell in common")
for city in commen:
    print(city)
    
print("\n\n")

#- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
diff=Nestle.difference(Unilever) 
print(f"cities Nestle sells in , but Unilver doens't sell in:")
for city in diff:
    print(city)
    
print("\n\n")