# walrus operator :=



# new to python 3.8 
# assignment expression aka walrus operator 
# assigns values to variables as part of a larger expressionhappy = True
#print(happy)

# while True:
#     food = input("what food do you like ?:")
#     if food == "quit":
#         break
#     foods.append(food)

foods =list()
while food := input("what food do you like ?:") != "quit":
    foods.append(food)
