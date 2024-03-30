# logical operators = used on conditional statements

#              and = checks two or more conditions if true 
#               or = checks if at least one condition is true  
#              not = true if condition is False, and vice versa


temp =int(input("What is the temprature today in celcius:"))

sunny = True


if temp <=0 or temp >= 30 :
    print("the temperature is bad ")
else:
    print("the temprature is good")



if not sunny:
    print("it's cloudy outside ")
else:
    print("It's sunny outside. ")    














