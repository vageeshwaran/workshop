pizzas=["Pepperoni", "Margherita", "BBQ Chicken"]
for pizza in pizzas:
    print(f"i like this{pizza} so much")
print("i really love pizzas and i enjoyed it")

squares=[]
for sq in range(1,11):
    squares.append(sq**2)
print(squares)

num=[]
for i in range(1,100):
    num.append(i)
print(num)
print(min(num))
print(max(num))
print(sum(num))

for i in range(3,30,3):
    print(i)

cube=[]    
for i in range(1,11):
    i=i**3
    cube.append(i)
print(cube)

cube=[value**3 for value in range(1,11)]
print(cube)

cars = [ "BMW", "Audi", "Mercedes", "Honda", "toyota", "chevrolet"]
print("the first three items in the list are:", cars[:3])
print("the middle three items in the list are:", cars[2:5])
print("the last three items in the list are:", cars[-3:])

new_pizza=pizzas[:]
pizzas.append("pizza1")
new_pizza.append("pizza2")
print("my favorite pizzas are the following")
for pizza in pizzas:
    print(pizza)
    
print("my friends favorite pizzas are:")
for new in new_pizza:
    print(new)