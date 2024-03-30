# Python quiz game 

questions = ("How many elements are there in periodic table :",
            "Which animal lays the largest egg on the planet?:",
            "What is the most abundant gas in Earth's atmosphere ?:",
            "How many bones are in the human body ?:",
            "Which planet in the solar system is the hottest ?:")


options = (("A.116","B.117","C.118","D.119"),
           ("A.crocodile ","B.turtle","C.ostrich","D.anaconda"),
           ("A.Hydrogen ","B.oxygen","C.Nitrogen","D.carbon"),
           ("A.203","B.207","C.206","D.204"),
           ("A.venus ","B.earth ","C.mars","D.mercury"))

answers = ("C","C","C","C","A")
guesses = []
score   = 0
question_num = 0


for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Entre ( A , B , C , D ):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("        RESULT        ")
print("----------------------")


print("guesses:", end="")
for guess in answers:
    print(guess,end=" ")
print()


score= int( score / len(question) * 1000)
print(f"Your score is :{score}%")


