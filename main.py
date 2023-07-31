#Q1
nestle={'KitKat':34_456_432,
        'Nescafe' : 14_106_132
        ,'Maggi' : 9_960_312
        ,'Nido' : 44_506_003}
#Q2
unilever ={'Lipton' : 23_456_000,
           'Breyers' : 1_235_891,
          'HellManns' : 17_241_412,
           'Marmite' : 11_715_324 }
#Q3
print('product sold by Unilever')
for key, value in unilever.items():
    print(f'{key}: {value}')
#Q4
print('-'*20)
print('product sold by Nestle')
for key, value in nestle.items():
    print(f'{key}: {value}')
#Q5
print('-'*20)
print('which of the companies has more products?')
nestleProducts= len(nestle)
uinileverProducts= len(unilever)
if nestleProducts > uinileverProducts:
    print('Nestle has more products than Unilever')
elif nestleProducts < uinileverProducts:
    print('Unilever has more products than Nestle')
else:
    print('Unilever and Nestle has the same number of products')
#Q6
print('-'*20)
topNestle=max(nestle.values())
for key, value in nestle.items():
    if topNestle == value:
      print(f'top selling product from Nestle: {key} with {value} sales')  
#Q7
print('-'*20)
topUnilever= max(unilever.values())
for key, value in unilever.items():
    if topUnilever == value:
      print(f'top selling product from Unilever: {key} with {value} sales')  
#Q8
print('-'*20)
nestleSet = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unileverSet = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
allCities = nestleSet.union(unileverSet)
for v in allCities:
 print(v)
#Q9
print('-'*15)
commonCities = nestleSet.intersection(unileverSet)
for v in commonCities:
 print(v)
#Q10
print('-'*20)
differenceCities = nestleSet.difference(unileverSet)
for v in differenceCities:
 print(v)
