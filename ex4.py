cars = 100.0
#number of cars avaialable
space_in_a_car = 4.0
#passengers per car
drivers = 30.0
#drivers available
passengers = 90.0
#passengers needed to transport
cars_not_driven = cars - drivers
#unused cars
cars_driven = drivers
#cars driving
carpool_capacity = cars_driven * space_in_a_car
#amnt of passengers total that we can take, 4 passengers per car for 30 drivers
average_passengers_per_car = passengers / cars_driven
#average passengers per car to transport all


print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"
