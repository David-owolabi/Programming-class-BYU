# def welcome(name):
#   """Returns a welcome message."""
#   print(f"Welcome {name} to the program!")
# user = input("Enter your name: ")
# welcome(user)


# def sub(first, second, third):
#   result = first + second - third
#   return result
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# z = int(input("Enter third number: "))
# total = sub(x, y, z)
# print(f"The result of the operation is: {total}")

# Your first line of Python code

def get_positive_number(prompt_text): 
    """prompts the user for a positive number"""
    value = float(input(prompt_text))
    while value < 0:
        print("Number cannot be NEGATIVE")
        value = float(input(prompt_text))
    return value
    
length = get_positive_number("Enter the Length of the rectangle: ")
width = get_positive_number(" Enter the width of the rectangle: ")
area = length * width
print(f"The area of the rectangle is: {area}")