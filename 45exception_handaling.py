# exception = events detected during execution that interrrupt the flow of program 
try:
    numerator = int(input("Enter a number to divide:"))
    denomnator = int(input("Enter a number to divide by :"))

    result= numerator/denomnator
    
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by zero idiot !")
except ValueError as e:
    print(e)
    print("you can't divide by alphabet you moron")
except Exception as e :
    print(e)    
    print("something went wrong :")
else:
    print(result)
finally:
    print("This will always execute ")