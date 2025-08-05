price = float(input("Enter the price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

def calculate_discount(price, discount_percentage):
    
    if discount_percentage >= 20:
        discount = price * (discount_percentage / 100)
        price = price  - discount
        return price
    else:
        price = price
        return price

final_price = calculate_discount(price, discount_percentage)
print(f'The price of the item is: {final_price}')

