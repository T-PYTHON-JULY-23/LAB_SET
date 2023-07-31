#lab set
#Q1
NestleDict = {"KitKat" : 34456432 ,
             "Nescafe" : 14106132,
             "Maggi" : 9960312,
             "Nido" : 44506003}

#Q2
UnileverDict = {"Lipton" : 23456000,
                "Breyers" : 1235891,
                "HellManns" : 17241412,
                 "Marmite" : 11715324}

#Q3
print("Unilever product sales:")
for product, sales in UnileverDict.items():
    print(product + ": " + str(sales) + " US Dollars")

#Q4
print("\nNestle product sales:")
for product, sales in NestleDict.items():
    print(product + ": " + str(sales) + " US Dollars")

#Q5
print("\nNumber of products:")
if len(NestleDict) > len(UnileverDict):
    print("Nestle has more products.")
elif len(NestleDict) > len(UnileverDict):
    print("Unilever has more products.")
else:
    print("Both companies have the same number of products.")

#Q6
topNestleProduct = max(NestleDict, key=NestleDict.get)
print("\nTop selling Nestle product:")
print(topNestleProduct + ": " + str(NestleDict[topNestleProduct]) + " US Dollars")

#Q7
topUnileverProduct = max(UnileverDict, key=UnileverDict.get)
print("\nTop selling Unilever product:")
print(topUnileverProduct + ": " + str(UnileverDict[topUnileverProduct]) + " US Dollars")

#Q8
unileverCities = set(["Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"])
nestleCities = set(["Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"])
print("\nCities where both Unilever and Nestle sell their products:")
for city in unileverCities.intersection(nestleCities):
    print(city)

#Q9    
print("\nCities where both Unilever and Nestle sell their products:")
for city in unileverCities.intersection(nestleCities):
    print(city)

#Q10
print("\nCities where Nestle sells, but Unilever doesn't sell:")
for city in nestleCities.difference(unileverCities):
    print(city)
