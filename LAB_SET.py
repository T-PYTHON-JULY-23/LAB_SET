




NestleProducts = { "KitKat" : 34456432 ,"Nescafe" : 14106132 ,"Maggi ": 9960312, "Nido" : 44506003 }
UnileverProducts = {"Lipton" : 23456000 , "Breyers" : 1235891 , "HellManns ": 17241412 ,"Marmite ": 11715324 }

citiesNestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
citiesUnilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for  key , val in NestleProducts .items():
 print(f" The products sales of Unilever : {key} numbers for that product: {val}") 
print("_"*50)
for  key , val in UnileverProducts.items():
  print(f" The products sales of Nestle : {key} numbers for that product: {val}") 

print("which of the companies has more products that the other company?")
if len(NestleProducts.keys()) == len (UnileverProducts.keys()):
 print(" The number of products is the same")
 
elif len(NestleProducts.keys()) > len (UnileverProducts.keys()):
    print(" Nestle company has more products that the other company")

else:
   print(" Unilever company has more products that the other company")

   #Print the top selling product from Nestle with sales figures.
   #Print the top selling product from Unilever with sales figures.


print (NestleProducts.items()) 


print (max(UnileverProducts.items())) 

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in. 
for city in (citiesNestle | citiesUnilever):
    print("The cities Unilever & Nestle sell their products in "+city) 


#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
for city in (citiesNestle & citiesUnilever):
    print("The cities that both Nestle & Unilver sell in common: "+city) 

#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
for city in (citiesNestle - citiesUnilever):
    print("The cities Nestle sells in , but Unilver doens't sell in: "+city) 


