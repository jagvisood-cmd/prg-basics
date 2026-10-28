###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

temp_celsius = float(input("Temperature in Celsius: ")) #getting input of temperature in celsius
convert_to_kelvin = temp_celsius + 273.15 # converting into kelvin
convert_to_fahrenheit = (temp_celsius*1.8)+32 #converting into fahrenheit
print(f"The temperature {temp_celsius} degree Celsius is {convert_to_kelvin} K.")
print(f"The temperature {temp_celsius} degree Celsius is {convert_to_fahrenheit} fahrenheit. ")
