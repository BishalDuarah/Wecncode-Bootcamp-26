# Input
order_amount = float(input("Enter order amount ($): "))
distance = float(input("Enter distance (km): "))
peak_hour = input("Is it peak hour? (yes/no): ").lower()

# Processing
if order_amount >= 500:
    delivery_fee = 0
else:
    # Base fee based on distance
    if distance <= 3:
        delivery_fee = 20
    elif distance <= 7:
        delivery_fee = 40
    else:
        delivery_fee = 70

    # Peak hour surcharge
    if peak_hour == "yes":
        delivery_fee += 15

# Output
print("\nDelivery Summary")
print("Order Amount: $", format(order_amount, ".2f"))
print("Distance:", distance, "km")
print("Peak Hour:", peak_hour)
print("Delivery Fee: $", format(delivery_fee, ".2f"))