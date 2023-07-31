Nestle_products={"KitKat":"34,456,432 US Dollars","Nescafe" : "14,106,132 US Dollars","Maggi" : "9,960,312 US Dollars","Nido" : "44,506,003 US Dollars"}
Unilever_products={"Lipton" : "23,456,000 US Dollars","Breyers" : "1,235,891 US Dollars","HellManns" : "17,241,412 US Dollars","Marmite" : "11,715,324 US Dollars"}
                   

print("products sold by Unilever")
for key in Unilever_products:
    print(key,":",Unilever_products[key])

print("products sold by Nestle")
for key in Nestle_products:
    print(key,":",Nestle_products[key])

print("which of the companies has more products than the other company")

if Nestle_products.values() in Nestle_products > Unilever_products.values():
    print("Nesltle has more products")
elif Nestle_products.values() in Nestle_products < Unilever_products.values():
    print(" Unilever has more products")
else:
    print("Same products amount")


print("top selling at Nestle:")
top_selling_Nestle= max(Nestle_products.items())
print(top_selling_Nestle)


print("top selling at Unilever:")
top_selling_Unilever=max(Unilever_products.items())
print(top_selling_Unilever)


Nestle_cities = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_cities = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


print("Citites Nestle sells thier products: ")
for i in Nestle_cities:
    print(i)

print("Citites Unilever sells thier products: ")
for i in Unilever_cities:
    print(i)

    
print("cities that both Nestle & Unilver sell in common: ")
citites_in_common = Nestle_cities.intersection(Unilever_cities)
print(citites_in_common)

print("cities Nestle sells in , but Unilver doens't sell in: ")
citites_difference = Nestle_cities.difference(Unilever_cities)
print(citites_difference)