# While loop = execute some code While some condition remains true.

age = int(input("Entre your age?:"))

while age < 0:
    print("Age can't be negative")
    age = int(input("Entre your age:"))

print(f"you are {age} years old")    

food = input("Entre a food you like (q to quit):")

while not food == "q":
    print(f"You like {food}")
    food=input("Entre another food you like (q to quit)")

print("bye")


num = int(input("Entre a # between 1-10 :"))

while num < 1 or num > 10:
    print(f"invalid entry bitch. {num } is not between 1 to 10")
    num = int(input("Entre a no between 1 - 10 :"))

print(F"your number is {num}")










