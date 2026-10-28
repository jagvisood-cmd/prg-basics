##
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results
import math
radius = int(input("r = "))
circumference = 2*math.pi*radius
area = math.pi * radius**2
print(f"circumference = {round(circumference,2)}, area = {round(area,2)}")
