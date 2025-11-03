from datetime import datetime
discount_days = [2,3] # Wednesday and Thursday
discount_rate = .1
tax_rate = .06
subtotal = 0
quantity = 1
while quantity != 0: # calculate the subtotal
  quantity = int(input("Enter the quantity: "))
  if quantity != 0:
    price = float(input("Enter the price: "))
    subtotal += quantity * price

print(f"Total order {subtotal:.2f}")
today = datetime.now() 
dow = today.weekday() # Monday is 0 and Sunday is 6
discount = 0
eligible = 50 - subtotal

if dow in discount_days:  # Wednesday or Thursday
  if subtotal >= 50:
    discount = round(subtotal * discount_rate, 2)
    print(f"Discount applied {discount:.2f}") 
  else:
    print(f"You need to purchase {eligible:.2f} worth of products to be eligible for a discount")

subtotal -= discount
tax = round(subtotal * tax_rate,2)
total = subtotal + tax - discount
print(f"Tax {tax:.2f}")
print(f"Total Due {total:.2f}")