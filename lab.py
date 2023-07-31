#1 :
nestle_product = {"KitKat":  34456432,
                  "Nescafe": 14106132 ,
                  "Maggi":   9960312,
                  "Nido":    44506003}
#2 : 
unilever_product = {"Lipton" : 23456000,
                    "Breyers" : 1235891,
                    "HellManns" : 17241412,
                    "Marmite" : 11715324}
#3 :
for key,value in nestle_product.items():
   print(f"{key} : $ {value} US Dollars")
#4 :
for key,value in unilever_product.items():
   print (f"{key} : ${value} US Dollars")
#5 :
if len(nestle_product) > len(unilever_product):
   print ("Nestle has more products than other company.")
elif len(unilever_product) > len(nestle_product) :
   print("Unilever has more products than other company.")
else:
   print("all the companies are the same")
#6 :

top_nestle_product= max(nestle_product,key=nestle_product.get)
print(f"\nThe top selling product from Unilever is {top_nestle_product} with sales figures of {nestle_product[top_nestle_product]} US Dollars.")

#7 :
top_unilever_product = max(unilever_product, key=unilever_product.get)
print(f"\nThe top selling product from Unilever is {top_unilever_product} with sales figures of {unilever_product[top_unilever_product]} US Dollars.")

#--- 8 ,9 ,10
Nestle_set = {"Saudi Arabia", "Oman ", "Kuwait ", "Egypt ", "Jordan ", "Sudan "}
Unilever_set = {"Saudi Arabia", "Kuwait ", "Iraq", "Morocco", "Yemen", "United Emirates"}
print("all the cities Unilever & Nestle sell their products in  : ")
for city in Nestle_set.union(Unilever_set):
   print(city)

print("\n the cities that both Nestle & Unilver sell in common :")
for city2 in Nestle_set.intersection(Unilever_set) :
   print(city2)
print("\n the cities Nestle sells in , but Unilver doens't sell in :")
nestle_cities = Nestle_set - Unilever_set
for city2 in nestle_cities :
   print (city2 , end= "")



   