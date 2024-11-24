from prac_09.unreliable_car import UnreliableCar

unreliable_car = UnreliableCar("Prius 1", 108000, 60)
print(unreliable_car.drive(80))

number_of_reliable_cars = 0

for i in range(100000):
    if unreliable_car.drive(1) > 0:
        number_of_reliable_cars += 1

print(number_of_reliable_cars/1000)