cars = [ "BMW", "Audi", "Mercedes", "Honda", "toyota", "chevrolet"]

new_cars=cars[:]
print(new_cars)
print(cars[4])
print(cars[-2])
cars[2]="benz"
print(cars)
cars.append("honda")
print(cars)
cars.insert(3, "kia")
print(cars)
cars.pop()
print(cars)
del cars[5]
print(cars)
cars.remove("Audi")
print(cars)
cars.sort()
print(cars)
cars.reverse()
print(cars)

print("the first three items in the list are:", cars[:3])