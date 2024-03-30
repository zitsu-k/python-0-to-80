#  vlidate user input exercise
#1. username should not contain more then 12 charecter 
#2. username should not contain space 
#3. username must not contain digits

username =input("Entre a user name:") 




if len(username) >12:
    print("word limit reached!\ncan't be more then 12 charecter's !")
elif not username.find(" ") == -1:
    print("username conno't contain spaces")
elif not username.isalpha() == True:
    print(f"User name connot contain numeric values!")

else:
    print(f"Welcome {username}!")    




