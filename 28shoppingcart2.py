# Shopping cart program

foods = []
prices = []
total = 0


while True:
    food = input("Entre a food to buy(q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Entre the price of a {food}:$"))
        foods.append(food)
        prices.append(price)


print("-----YOUR CART-----")
for food,price in foods:
    # print(food, end=" , ")
        print(end="")
        print((f"{food:<}:${price:^}"))


print("-----------------------")


for price in prices:
    total += price

print(f"your total is :${total}")


