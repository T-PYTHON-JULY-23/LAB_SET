## Using what you've learned during . Please do the following :
'''- Create a variable to hold the values of Nestle products (use a dicitionary)
- Create a variable to hold the values of Unilever products (Use a dictionary)
- Print each product sold by Unilever and the sales figures / numbers  for that product.
- Print each product sold by Nestle and the sales figures / numbers  for that product.'''


nestle ={"KitKat": 34456432,
         "Nescafe":14106132,
         "Maggi":9960312 ,
        "Nido ": 44506003
           }
unilever={"Lipton" : 23456000,
           "Breyers" : 1235891, 
           "HellManns":17241412,
           "Marmite" :11715324
           }

for key, value in nestle.items():
    print(key, ":", value, "US Dollars")

print("-"*30)
for key, value in unilever.items():
    print(key, ":", value, "US Dollars")

#- Print which of the companies has more products that the other company.
if len(nestle) > len(unilever):
    print("nestle company more ")
elif len(nestle) < len(unilever):
    print("unilever company more")
else:
    print("\nThe same companies")


print("-"*30)
#- Print the top selling product from Nestle with sales figures.
top_selling_nestle=[]
for key in nestle:
    top_selling_nestle.append(nestle[key])
print("top selling product from Nestle:", max(top_selling_nestle))


#- Print the top selling product from Unilever with sales figures.
top_selling_unilever=[]
for key in unilever:
    top_selling_unilever.append(unilever[key])
print("top selling product from unilever:", max(top_selling_unilever))

print("-"*30)

nestle_cities= {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_cities= {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

cite_union = nestle_cities.union(unilever_cities)
print("Unilever & Nestle sell their products in:")
for i in cite_union:
    print(i)
 
print("-"*30)

cite_intersection= nestle_cities.intersection(unilever_cities)
print("the cities that both Nestle & Unilver sell in common")
for inter in cite_intersection:
    print(inter)

print("-"*30)

cite_difference= nestle_cities-(unilever_cities)
print("the cities Nestle sells in , but Unilver doens't sell in")
for diff in cite_difference:
    print(diff)