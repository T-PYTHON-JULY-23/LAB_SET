
Sales_Of_Nestle= { 

'KitKat' : 34456432,

'Nescafe' : 14106132,

'Maggi' : 9960312,

'Nido' : 44506003 }

Sales_Of_Unilever= {

'Lipton' : 23456000, 

'Breyers' : 1235891, 

'HellManns' : 17241412, 

'Marmite' : 11715324 }

Countries_Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

Countries_Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


print("Printing each product sold by Unilever and the sales figures: ")
for key in Sales_Of_Unilever:
    print(key, ":", Sales_Of_Unilever[key], "US Dollars")

print('-'*10)

print("Printing each product sold by  Nestle and the sales figures: ")
for key in Sales_Of_Nestle:
    print(key, ":", Sales_Of_Nestle[key], "US Dollars")

print('-'*10)
print("Printing which of the companies has more products: ")

Count_Unilever_Products=0 
Count_Nestle_Products=0 

for key in Sales_Of_Unilever:
    Count_Unilever_Products +=1

for key in Sales_Of_Nestle:
    Count_Nestle_Products +=1

if Count_Nestle_Products > Count_Unilever_Products:
    print("Nestle has more products ")
elif Count_Nestle_Products < Count_Unilever_Products:
    print("Unilever has more products ")
elif Count_Nestle_Products == Count_Unilever_Products:
    print("Unilever and Nestle has the same number of products ")

print('-'*10)
print("The top selling product from Nestle") 

Top_Nestle = max(Sales_Of_Nestle)
print(Top_Nestle)

print('-'*10)
print("The top selling product from Unilever") 
# مشكله
Top_Unilever = max(Sales_Of_Unilever)
print(Top_Unilever)

print('-'*10)
print("Unilever and Nestle the list of all the cities they sell their products in: ")
Unilever_and_Nestle = Countries_Nestle.union(Countries_Unilever)
for val in Unilever_and_Nestle:
    print("- ",val)

print('-'*10)
print("Unilever and Nestle the list of the cities they both sell their products in: ")
Unilever_common_Nestle = Countries_Nestle.intersection(Countries_Unilever)
for val in Unilever_common_Nestle:
    print("- ",val)

print('-'*10)
print("Ucities Nestle sells in , but Unilver doens't sell in: ")
Unilever_common_Nestle = Countries_Nestle.intersection(Countries_Unilever)
for val in Unilever_common_Nestle:
    print("- ",val)