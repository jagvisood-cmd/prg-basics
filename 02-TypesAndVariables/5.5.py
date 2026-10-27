product_price = float(input('Enter price : '))
discount_on_price = int(input('Enter discount % : '))
calculating_discount = product_price*discount_on_price/100
price_with_discount = product_price - calculating_discount
reduction = product_price - price_with_discount
print(f"Price with discount: {round(price_with_discount, 2)}")
print(f"Reduction: {round(reduction, 2)}")