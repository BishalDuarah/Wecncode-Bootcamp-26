# Input
product_name = input("Enter product name: ")
unit_price = float(input("Enter unit price ($): "))
quantity = int(input("Enter quantity: "))
shipping_fee = float(input("Enter shipping fee ($): "))

# Processing
subtotal = unit_price * quantity
grand_total = subtotal + shipping_fee
loyalty_points = int(grand_total // 10)

# Output
print("\nCheckout Summary")
print("Product:", product_name)
print("Subtotal: $", format(subtotal, ".2f"))
print("Grand Total: $", format(grand_total, ".2f"))
print("Loyalty Points:", loyalty_points)