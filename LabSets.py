"""# LAB_SET


### Kate, Dalia & Monica are work associates . They all work at a consultancy company.

## Kate has the products sales of Nestle :

##### KitKat : 34,456,432 US Dollars
##### Nescafe : 14,106,132 US Dollars
##### Maggi : 9,960,312 US Dollars
##### Nido : 44,506,003 US Dollars

      

## Dalia has the products sales of Unilever :

##### Lipton : 23,456,000 US Dollars
##### Breyers : 1,235,891 US Dollars
##### HellManns : 17,241,412 US Dollars
##### Marmite : 11,715,324 US Dollars
      

## Monica has 2 tables containing the countries in which Unilever and Nestle sell the products:
##### Nestle : "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
##### Unilever : "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"


## Using what you've learned during . Please do the following :
- Create a variable to hold the values of Nestle products (use a dicitionary)
- Create a variable to hold the values of Unilever products (Use a dictionary)
- Print each product sold by Unilever and the sales figures / numbers  for that product.
- Print each product sold by Nestle and the sales figures / numbers  for that product.
- Print which of the companies has more products that the other company.
- Print the top selling product from Nestle with sales figures.
- Print the top selling product from Unilever with sales figures.
- Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.

"""
nestla_products={
    'KitKat' : 34456432,
    "Nescafe" : 14106132,
    'Maggi' : 9960312,
    'Nido' : 44506003,

}
unilever_products={
    'Lipton' : 23456000 ,
    'Breyers' : 1235891,
    'HellManns' : 17241412,
    'Marmite' : 11715324 ,
}
print("Nestlaa seals numbers ".title())
for key ,value in nestla_products.items():
    print(key ,":", value)
print('-'*15)

print("Unilever seals numbers ".title())
for key ,value in unilever_products.items():
    print(key ,":", value)
if len(unilever_products)>len(nestla_products):
    print("Unilever has more prodecuts ")
elif len(unilever_products)<len(nestla_products):
    print("Nestla has more products ")
else :
    print("Nestla and Unilver have same number of proudctes")
product_name,top_sale ='None',0 
for item,sales in nestla_products.items():
    if sales>top_sale:
        top_sale=sales
        product_name=item
print(f'Nestla Top item is {product_name} with {top_sale} sales\n')

product_name,top_sale ='None',0 
for item,sales in unilever_products.items():
    if sales>top_sale:
        top_sale=sales
        product_name=item
print(f'Unilever Top item is {product_name} with {top_sale} sales')

Nestle={ "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever={ "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
print("all the cities Unilever & Nestle sell their products in are : ".title())
for city in Nestle | Unilever:
    print(f"{city} , ", end='')

print("\nThe cities that both Nestle & Unilver sell in common are :".title())

for city in Nestle & Unilever:
    print(f"{city} , ", end='')
print("\nthe cities Nestle sells in , but Unilver doens't sell in are : ".title())

for city in Nestle - Unilever:
    print(f"{city} , ", end='')

