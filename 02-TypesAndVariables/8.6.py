###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption in litres: '))
total_fuel_consumption = (distance/100)*fuel_consumption
total_cost = total_fuel_consumption * fuel_price
print(f"The total of fuel consumed for transport is {total_fuel_consumption}")
print(f"The total cost of fuel is {round(total_cost,2)}")