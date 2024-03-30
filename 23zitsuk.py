name= input("what is your name?:")
age = input("please entre your age?:")

if int(age) < 18 :
    print(f"dear {name} you are not eligible to enroll in this program beacause you are {age} year's old ")
else:
    print(f"Thank you {name} for registring for our program")    

name = name.capitalize()
while int(age) > 18:
    course = input("which program you want to enroll in(python,java,c++,c,q to quit)? :")
    if course == "python":
        print(f"{name} you have been enrolled in the python programing and it will take 6 months to  to complete")
    elif course == "java":
        print(f"{name} you have been enrolled in the java programing and it will take 6 months to complete")
    elif course == "c++":
        print(f"{name} you have been enrolled in the c++ programing and it will take 6 months to complete")
    elif course == "c":
        print(f"{name} you have been enrolled in the c programing and it will take 6 months to complete")
    elif course == "":
        print(f"{name} , you have not selected the course priscribed above")            
    else:
        break

print("thank you for registration")













