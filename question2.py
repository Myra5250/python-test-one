#Question 2
# Using a function, create a program that calculates the volume of a cylinder.

radius = int(input("Enter the radius: "))
height = int(input("Enter the height: "))
import math
pie = math.pi
volume = pie * radius **2 * height
print(f"The volume of a cylinder is {volume}")