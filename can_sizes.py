import math

def main():
    can_eff("#1 Picnic",6.83, 10.16)
    can_eff("#1 Tall",7.78, 11.91)
    can_eff("#2",8.73, 11.59)
    can_eff("#2.5",10.32, 11.91)
    can_eff("#3 Cylinder",10.49, 17.78)
    can_eff("#5",13.02, 14.29)
    can_eff("#6Z",5.40, 8.89)
    can_eff("#8Z short",6.83, 7.62)
    can_eff("#10",15.72, 17.78)
    can_eff("#211",6.83, 12.38)
    can_eff("#300",7.62, 11.27)
    can_eff("#303",8.10, 11.11)


def can_eff(name,radius, height):
    """
    Calculate the efficiency of a cylinder (can) given its radius and height.
    Efficiency = Volume / Surface Area
    """
    volume = can_volume(radius, height)
    area = can_area(radius, height)
    efficiency = volume / area
    print(f"{name}   Volume: {volume:.2f} cm^3, area: {area:.2f} cm^2, efficiency: {efficiency:.2f} cm^-1")

def can_volume(radius, height):
    """
    Calculate the volume of a cylinder (can) given its radius and height.
    Volume = π * r^2 * h
    """
    volume = math.pi * radius**2 * height
    return volume

def can_area(radius, height):
    """
    Calculate the surface area of a cylinder (can) given its radius and height.
    Surface Area = 2 * π * r * (r + h)
    """
    area = 2 * math.pi * radius * (radius + height)
    return area
main()