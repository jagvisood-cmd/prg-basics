parking_hours = int(input("Enter hours of parking: "))

if parking_hours <= 2:
    print("Fee: 5 PLN")
elif parking_hours >= 3 and parking_hours <= 6:
    print("Fee: 15 PLN")
else:
    print("Fee: 20 PLN")