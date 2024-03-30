#if = Do some  code only IF some condition is True 
#     Else do something else

age = int(input("Entre your age?: "))

if age >= 100:
    print("too old")  
elif age >= 18:
    print("you are now signed up! ")
elif age < 0:
    print("you are not born yet ")    
else:
    print("you must be 18+ to sign up")


response = input("would you like food?(Y/N):")

if response == "Y":
    print("Have some food ")
elif response == "N":
    print("No food for you !")


name = input("Please entre your name:")
if name == "":
    print("type you name you motherfucking bitch!")
else:
    print(f"hello {name}")

for_sale = True


if for_sale:
    print("This item is for sale!")
else:
    print("This item is nor for sale")

online = True

if online:
    print("The user is online ")
else:
    print("that mutherfuker is offline")



























