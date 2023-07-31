
Nestle_product_sales = {((" Kitkat" , 34456432 ) , ("Nescafe " , 14106132) , (" Maggi", 9960312 ) , ( "Nido", 44506003))}
Unilever_product_sales = {(("Lipton" , 23456000 ) , ("Breyers " , 1235891) , (" Breyers", 17241412 ) , ( "Breyers", 11715324))}

print(Nestle_product_sales)
print(Unilever_product_sales)
      
if Nestle_product_sales > Unilever_product_sales:
      print ( "Sales of Nestle company are higher" )
if Nestle_product_sales < Unilever_product_sales:
      print ( "Sales of unilever company are higher")
else: 
    print ("Both companies have the same number of products" )
    
for item in Nestle_product_sales:
    print(max(item))
 
for item in Unilever_product_sales:
    print(max(item))
      
   
Nestle_countries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

Unilever_countries = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

all_countries = (Nestle_countries.union(Unilever_countries))
print ( "all the countries Unilever & Nestle sell their products in ")
for country in all_countries:
 print (country)


common = (Nestle_countries.intersection(Unilever_countries))
print ( "the countries that both Nestle & Unilver sell in common")
for country in common:
 print (country)
 
shell_in = (Nestle_countries.difference(Unilever_countries))
print ("the countries Nestle sells in , but Unilver doens't sell in" )
for country in shell_in:
 print (country)




