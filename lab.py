nestle = {

    "KitKat" : 34456432,
    "Nescafe" : 14106132,
    "Maggi" : 9960312 ,
    "Nido" : 44506003

}

unilever = {    

    "Lipton" : 23456000,
    "Breyers" : 1235891,
    "HellManns" : 17241412,
    "Marmite" : 11715324

}

nestle_set = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_set = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
# wrong code >
# print(unilever)
# print(nestle)

print("Nestle products :")
for product in nestle.keys():
    print(f"{product} : {nestle[product]}$")

print("Unilever products :")
for product in unilever.keys():
    print(f"{product} : {unilever[product]}$")

if len(unilever) > len(nestle):
    print(f"\nUnilever has more product than Nestle\n")
elif len(unilever) < len(nestle):
    print(f"\nNestle has more product than Unilever\n")
else:
    print(f"\nUnilever and Nestle have the same product amount\n")

# wrong code >
# print(max(nestle), f"{max(nestle.values())} USD")
# print(max(unilever), f"{max(unilever.values())} USD")
print("--"*20)

nestle_top_sales = max(nestle.values())
for product in nestle.keys():
    if (nestle[product] == nestle_top_sales):
        print(f"nestle top seling product : {product} with {nestle[product]}$")


unilever_top_sales = max(unilever.values())
for product in unilever.keys():
    if (unilever[product] == unilever_top_sales):
        print(f"nestle top seling product : {product} with {unilever[product]}$")

print("--"*20)

nestle_unilever_uine = nestle_set | unilever_set

print("All the cities Unilever & Nestle sell their products in.")
for city in nestle_unilever_uine:
    print('-', city)

nestle_unilever_Intersection = nestle_set & unilever_set

print("the cities that both Nestle & Unilver sell in common.")
for city in nestle_unilever_Intersection:
    print('-', city)

inNestle_butNot_inUnilever = nestle_set - unilever_set

print("the cities Nestle sells in , but Unilver doens't sell in.")
for city in inNestle_butNot_inUnilever:
    print('-', city)

    