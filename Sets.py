# LAB_SET
# Kate, Dalia & Monica are work associates . They all work at a consultancy company.
# Kate has the products sales of Nestle :
# KitKat : 34,456,432 US Dollars
# Nescafe : 14,106,132 US Dollars
# Maggi : 9,960,312 US Dollars
# Nido : 44,506,003 US Dollars
# Dalia has the products sales of Unilever :
# Lipton : 23,456,000 US Dollars
# Breyers : 1,235,891 US Dollars
# HellManns : 17,241,412 US Dollars
# Marmite : 11,715,324 US Dollars     
# Monica has 2 tables containing the countries in which Unilever and Nestle sell the products:
# Nestle : "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
# Unilever : "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"
# Using what you've learned during . Please do the following :
Kate_Nestle_Product = {"KitKat" : 34456432,"Nescafe" : 14106132 ,"Maggi" : 9960312  ,"Nido" : 44506003, }
Dalia_Unilever_Product = { "Lipton" : 23456000 , "Breyers" : 1235891 , "HellManns" : 17241412 , "Marmite" : 11715324,}



Unilever_Countries ={ "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
Nestle_countries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

# Create a variable to hold the values of Nestle products (use a dicitionary)
Nestle_holder = {"":""}
# Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever_holder = {"":""}
# Print each product sold by Unilever and the sales figures / numbers for that product.
print("===Unilever Product===")
for key,value in Dalia_Unilever_Product.items():
    print(key,"${}".format(value))

# Print each product sold by Nestle and the sales figures / numbers for that product.
print("===Nestle Product===")
for key,value in Kate_Nestle_Product.items():
    print(key,"${}".format(value))

# Print which of the companies has more products that the other company.
print("---"*15)
Nestle_comp=0
Unilever_comp=0 
for i in Kate_Nestle_Product:
    Nestle_comp += 1
    for j in Dalia_Unilever_Product:
        Unilever_comp += 1
        if Nestle_comp > Unilever_comp:
            print("Kate have more products")
            
            if Nestle_comp < Unilever_comp:
                print("Dalia have more products")
else:
    print("they both have the same products number")

    
print("---"*15)

# Print the top selling product from Nestle with sales figures.
Nestle_Top_sales = max(Kate_Nestle_Product.values())
print("Top selling product from Nestle is ${}".format(Nestle_Top_sales))


# Print the top selling product from Unilever with sales figures.
Unilever_Top_sales = max(Dalia_Unilever_Product.values())
print("Top selling product from Unilever is ${}".format(Unilever_Top_sales))

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print("---"*15)

nestle_unilever_countries = Nestle_countries | Unilever_Countries
print("This is the all the countries that both companies sells in it: ")
for i in nestle_unilever_countries:
    print("||",i,"||",end=" ")

print("---"*15)
# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print("||", Unilever_Countries & Nestle_countries , "||")
print("---"*15)
# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print(Nestle_countries.difference(Unilever_Countries))
