nestle_products = {
    "KitKat": 34456432,
    "Nescafe": 14106132,
    "Maggi": 9960312,
    "Nido": 44506003
}
#--------------------------------
unilever_products = {
    "Lipton": 23456000,
    "Breyers": 1235891,
    "HellManns": 17241412,
    "Marmite": 11715324
}

nestle_cities = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_cities ={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
#-------------------------------
def product_sold_by_Unilever(dict):
    count =1
    print("Unilever products:")
    for product, sales in unilever_products.items():
        print(f"{count} - {product}: {sales} US Dollars")
        count+=1


product_sold_by_Unilever(unilever_products)

#------------------------------------
def product_sold_by_Nestle(dict):
    count =1
    print("\nNestle products:")
    for product, sales in nestle_products.items():
        print(f"{count} - {product}: {sales} US Dollars")
        count+=1

product_sold_by_Nestle(nestle_products)

#-------------------------------------------------
def companies_has_more_products():
    if len(nestle_products) > len(unilever_products):
        print("\nNestle has more products than Unilever")
    elif len(nestle_products) < len(unilever_products):
        print("\nUnilever has more products than Nestle")
    else:
        print("\nNestle and Unilever have the same number of products")

companies_has_more_products()

#---------------------------------
top_nestle_product = max(nestle_products, key=nestle_products.get)
top_nestle_sales = nestle_products[top_nestle_product]
print(f"\nThe top selling Nestle product is {top_nestle_product} with {top_nestle_sales} US Dollars in sales")
#--------------------------------
top_unilever_product = max(unilever_products, key=unilever_products.get)
top_unilever_sales = unilever_products[top_unilever_product]
print(f"\nThe top selling Unilever product is {top_unilever_product} with {top_unilever_sales} US Dollars in sales")


# --------------------------------------------------------------------
print(f"\nCities where both Nestle and Unilever sell their products: {nestle_cities.union(unilever_cities)}")
print(f"\nAll cities where Nestle sells its products: {nestle_cities}")
print(f"\nAll cities where Unilever sells its products: {unilever_cities}")

# ---------------------------------------------------------------------
common_cities = nestle_cities.intersection(unilever_cities)
print("\nCities where both Nestle and Unilever sell their products:")
for city in common_cities:
    print(city)
#---------------------------------
nestle_only_cities = nestle_cities.difference(unilever_cities)
print("\nCities where Nestle sells its products, but Unilever doesn't:")
for city in nestle_only_cities:
    print(city)
