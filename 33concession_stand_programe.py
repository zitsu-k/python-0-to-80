# Concession stand programe

# dicitionary {key:value}

menu= {"popcorn":2.34,
        "pizza":  4,
        "drinks": 1,
        "hamburger": 5}

cart = []
total = 0

print("--------------------MENU--------------------")
for key,value in menu.items():
    print(f"{key:10}:  ${value:.2f}")
print("--------------------------------------------")

while True:
    food = input("Please entre the item you want to buy(press q to quit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("==========================================")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is : ${total:.2f}")
print("==========================================")