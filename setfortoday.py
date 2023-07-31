Nestle_products = {"KitKat" : 34456432,
 "Nescafe" : 14106132,
  "Maggi":9960312 ,
   "Nido":44506003
   }
Unilever_products = {"Lipton" : 23456000,
                     "Breyers" : 1235891 ,
                     "HellManns" : 17241412,
                     "Marmite" : 11715324
                     }
print ("The product sold by Unilever and the sales figures:")
for key, value in Unilever_products.items() :
       print(f"product is: {key} sales figures: {value} $")
       
print("The product sold by Nestle and the sales figures:")
for key, value in Nestle_products.items ():
    print (f"product is: {key} sales figures: {value} $")

print ("The company is has more products:")
if len (Nestle_products)>len (Unilever_products) :
  print ("Nestle company has more prodect ")
elif len(Nestle_products)<len (Unilever_products) :
    print ("Unilever company has more prodect ")
else:
    print ("Nestle and Unilever are the same")
top_selling=max (Nestle_products.values ())
top_prodect= {prod for prod in Nestle_products if Nestle_products [prod]==top_selling}
print(f"the top selling product from Nestle is :{top_prodect} {top_selling} $")
top_selling_Unilever=max(Unilever_products. values ())
top_prodect_Unilever= {prod for prod in Unilever_products if Unilever_products[prod]==top_selling_Unilever}
print(f"the top selling product from Unilever is :{top_prodect_Unilever} {top_selling_Unilever} $")


Nestle_cities={"Saudi Arabia","Oman", "Kuwait","Egypt","Jordan","Sudan"}
Unilever_cities={"Saudi Arabia", "Kuwait", "Iraq","Morocco", "Yemen","United Emirates"}
#Nestles_unilever = Nestle_cities.union(Unilever_cities)
print("all the cities Unilever & Nestle sell their products in:")
for city in Nestle_cities & Unilever_cities:
    print(city)
#print ("the cities Unilever & Nestle sell their products in:",Nestles_unilever)
#Nestles_unileverr = Nestle_cities.intersection(Unilever_cities)
print("the cities that both Nestle & Unilver sell in common:")
for city in Nestle_cities | Unilever_cities:
    print (city)
#print (" the cities that both Nestle & Unilver sell in common:", Nestles_unileverr)
#Nestles_unileverrr = Nestle_cities.difference(Unilever_cities)
print("the cities Nestle sells in , but Unilver doens't sell in:")
for city in Nestle_cities - Unilever_cities:
    print(city)