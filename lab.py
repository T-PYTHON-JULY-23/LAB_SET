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

print(unilever)
print(nestle)

if len(unilever) > len(nestle):
    print(f"\nUnilever has more product than Nestle\n")
elif len(unilever) < len(nestle):
    print(f"\nNestle has more product than Unilever\n")
else:
    print(f"\nUnilever and Nestle have the same product amount\n")

print(max(nestle), f"{max(nestle.values())} USD")
print(max(unilever), f"{max(unilever.values())} USD")

print(nestle_set | unilever_set)
print(nestle_set & unilever_set)
print(nestle_set - unilever_set)
    