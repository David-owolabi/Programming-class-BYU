import math
def main():
  name = "#1 picnic"
  radius = 6.83
  height = 10.16
  can_eff(name, radius, height)#Good function

  can_eff("#2 soup", 4.45, 12.38)#better function, the aim is to make it shorter and readable
  

def can_eff(name, radius, height):
  volume = can_vol(radius, height)
  area = can_area(radius, height)
  eff = volume / area
  print(f"{name}, volume: {volume:.2f}, area: {area:.2f}, efficiency: {eff:.2f}")

def can_vol(radius, height):
  volume  = math.pi * radius**2 * height
  return volume

def can_area(radius, height):
  area = 2*math.pi*radius*(radius + height)
  return area

main()
