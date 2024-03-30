# fruits =     [ "apple ", " orrange ", "  banana" , " coconut"]
# vegetables = [ "celery", "eggplant" , "tomato ", "patatoes"]
# meats =      ["fish ", "chicken", "turkey"]

# groceries = [fruits,vegetables,meats]

groceries = [["apple", "orrange","banana","coconut"],
             ["celery","eggplant","tomato","potato"],
             ["chicken","fish","turkey"]]

# print(groceries[0][0])
for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()


# for x in groceries:
#     print(x)







