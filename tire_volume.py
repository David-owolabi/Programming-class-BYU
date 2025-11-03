from datetime import datetime 
import math
tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15) "))
tire_volume = math.pi * tire_width**2 * aspect_ratio*(tire_width * aspect_ratio + 2540 * wheel_diameter)/10000000000

print(f"The approximate volume is {tire_volume:.2f} liters")
current_date_time = datetime.now()
formatted_date = current_date_time.strftime("%Y-%m-%d")

with open("log_data.txt", "a") as file:
  file.write(f"\nDate: {formatted_date}\nTire Width: {tire_width}\nAspect ratio: {aspect_ratio}\nWheel diameter: {wheel_diameter}\nTire volume: {tire_volume:.2f}\n")
  print("Data successfully added to log_data.txt")