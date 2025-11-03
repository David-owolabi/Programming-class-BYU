from datetime import datetime 
import math
tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
tire_volume = math.pi * tire_width**2 * aspect_ratio*(tire_width * aspect_ratio + 2540 * wheel_diameter)/10000000000

print(f"The approximate volume is {tire_volume:.2f} liters")
current_date_time = datetime.now()
formatted_date = current_date_time.strftime("%Y-%m-%d")

with open("volume.txt", "a") as file:
  file.write(f"\nDate: {formatted_date}\nTire Width: {tire_width}\nAspect ratio: {aspect_ratio:.2f}\nWheel diameter: {wheel_diameter}\nTire volume: {tire_volume:.2f}\n")
  print("Data successfully added to log_data.txt")

  if tire_width == 225 and aspect_ratio == 135 and wheel_diameter == 15:
    price = 108.64
    print(f"Price of the tire is: ${price}")
  elif tire_width == 235 and aspect_ratio == 176.25 and wheel_diameter == 15:
    price = 80
    print(f"Price of the tire is: ${price}")
  elif tire_width == 205 and aspect_ratio == 112.75 and wheel_diameter == 16:
    price = 114.50
    print(f"Price of the tire is: ${price}")
  elif tire_width == 195 and aspect_ratio == 107.25 and wheel_diameter == 16:
    price = 94.50
    print(f"Price of the tire is: ${price}")
  else:
    price = None
    print("Tire price not found in the database.")

buy_tires = input("Do you want to buy tires with these specifications? (yes/no): ").strip().lower()
if buy_tires == "yes" and price != None:
  contact_information = input("Please provide your phone number: ")
  with open("volume.txt", "a") as file:
    file.write(f"Customer Phone Number: {contact_information}\n")
    print("Thank you for your purchase! We will contact you soon.")
else:
  print("Thank you for using the tire volume calculator.")
  