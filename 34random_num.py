import random

#print(help(random))


# low = 1 
# high = 100

# option = ("rock", "paper ", "scissors")

# cards = ["2","3","4","5","6","7","8","9","10","K","J","Q","A"]


#number = random.randint(low,high)
# number = random.random()
# option = random.choice(option)
# random.shuffle(cards) 
# print(cards)

low = 1 
high = 100
guesses = 0
number = random.randint(low,high)
while True:
    guess = int(input(f"Entre a number between ({low} - {high})"))
    guesses += 1 
    if guess < number:
        print(f"{guess} is too low ")
    elif guess> number:
        print(f"{guess} is too high ")
    else:
        print(f'{guess} is correct')
        break

print(f" This round took you {guesses} round")

















