###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
cm_to_total_inches = cm/2.54
feet = int(cm_to_total_inches // 12)
inches = int(cm_to_total_inches % 12)
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {round(inches,0)} inches')