dogs_age = int(input("Enter the dog's age in human years: "))

#For the first two years, a dog's life is equal to 10.5 human years. 
#After that, each dog year is equal to 4 human years.

if dogs_age <= 2:
    dogs_real_age = dogs_age * 10.5
else:
    dogs_real_age = 2 * 10.5 + (dogs_age - 2) * 4
print(f"The dog's age in dog's years is {int(dogs_real_age)}")