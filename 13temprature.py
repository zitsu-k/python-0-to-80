unit = input("is the tempreture is in Celsius , Feranite (C/F): ")
temp = float(input("Entre the temprature: "))


if unit == "C":
    temp = (temp * 9/5) + 32
    unit = "F"
    print(f"the temp is {temp} {unit}")

elif unit == "F":
    temp = (5*temp - 160)/9
    unit = "celcius"
    print(f"the temp is {temp} {unit}")

else:
    print(f"the entred unit {unit} is invalid ")




































