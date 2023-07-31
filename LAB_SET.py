Nestle_products  = {
"KitKat" : 34456432,
"Nescafe" : 14106132,
"Maggi" : 9960312,
"Nido" : 44506003
}

Unilever_products = {
    "Lipton" : 23456000,
"Breyers" : 1235891,
"HellManns" : 17241412,
"Marmite" : 11715324
}
print("*"*25)
avg_Nestle:int = [Nestle_value for Nestle_value in Nestle_products.values()]
print("The average of the price Nestle products is :",sum(avg_Nestle)/len(avg_Nestle))

avg_Unilever:int = [Unilever_value for Unilever_value in Unilever_products.values()]
print("The average of the price Unilever products is :",sum(avg_Unilever)/len(avg_Unilever))
if len(avg_Unilever) > len(avg_Nestle) :
    print("The prodcuts of  Unilever is greater than Nestle")
else:
    print("The prodcuts of  Nestle is greater than Unilever")
print("*"*3)
# Print the top selling product from Nestle with sales figures.
print(f"the top selling product from Nestle :{max(avg_Nestle)}")
# Print the top selling product from Unilever with sales figures.
print(f"the top selling product from Unilever :{max(avg_Unilever)}")

Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
print(Nestle | Unilever)
print(Nestle & Unilever)
print(Nestle - Unilever)
