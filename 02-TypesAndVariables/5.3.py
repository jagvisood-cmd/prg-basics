###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
volume_cuboid = a*b*c
surface_area_of_cuboid = (2*(a*b))+(2*(a*c))+(2*(b*c))
print(f"The volume of a cuboid is {volume_cuboid}")
print(f"The surface area of a cuboid is {surface_area_of_cuboid}")