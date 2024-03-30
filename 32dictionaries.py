#dictionary = a collection of {key:value } pairs 
#             ordered and changeable . No duplicates

capitals = {"USA":"Washington DC",
            "INDIA":"NEW DELHI",
            "PAKISTAN":"lahor",
            "Nepal":"Katmandu",
            "Japan":"Tokeyo"}


# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))
#this is used to get the value of key from the dictionary
# if an unkown key is asked then the answer returned will be none 

if capitals.get("Japan"):
    print("that capital exist ")
else:
    print("That capital dosn't exist")

capitals.update({"Germany":"Berlin"})
#we can add elements with add method as well as update a key and it's value with this 
capitals.update({"china":"benjing"})
capitals.pop("INDIA")
capitals.popitem()
capitals.clear()

key = capitals.keys()
for key in capitals.keys():
    print(key)


values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key,value in capitals.items():
    print(f"{key}:{value}")
















