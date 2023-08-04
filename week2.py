
#dicts
Nestle= {
    "Kitkat":34_456_432,
    "Nescafe":14_106_132,
    "Maggi":9_960_312,
    "Nido":44_506_003,
 }

Unilever= {
    "Lipton":23_456_000,
    "Breyers":1_235_891,
    "HellManns":17_241_412,
    "Marmite":1_715_324,
 }

#sets
UnileverCountries ={ "Saudi Arabia", "Kuwait", 
                    "Iraq", "Morocco", "Yemen", "United Emirates"}
NestleCountris ={ "Saudi Arabia", "Oman", "Kuwait",
                  "Egypt", "Jordan", "Sudan"}


def AllIitems (AllDictElements):
 print("The list of all products and its sales: ")
 for key, value in AllDictElements.items():
    print(f"{key}, ${value}")

def countProducts(company1,company2) :
  if len(company1)>len(company2):
    print("The company that has more products is:  ",company1)
  elif len(company1)<len(company2):
     print("The company that has more products is:  ",company2)
  elif len(company1)==len(company2):
     print("The two companies has the same amount of products")   
   

def TopSelling (company):
  
  #for key, value in company.items():
   #maxvValue=0
   #maxKey=""
   #if value > maxvValue:
     #maxvValue=value
     #maxKey=key

  print(f"The top selling product is  {max(company.keys())} :{max(company.values())}")
   
    
def countriesUnion(country1,country2):
  
  cominationCountries=country1.union(country2)
  print("The combination of countris in both companies",cominationCountries)


def countriesIntersection(country1,country2):
  
  intersectionCountries=country1.intersection(country2)
  print("The intersection of countris in both companies",intersectionCountries)  


def countriesDifference(country1,country2):
  
  differenceCountries=country1.difference(country2)
  print("he cities Nestle sells in that is Unilver doens't sell in",differenceCountries)  










AllIitems(Nestle)
AllIitems(Unilever)
countProducts(Nestle,Unilever)
TopSelling (Nestle)
TopSelling (Unilever)

countriesUnion(UnileverCountries,NestleCountris)
countriesIntersection(UnileverCountries,NestleCountris)
countriesDifference(UnileverCountries,NestleCountris)