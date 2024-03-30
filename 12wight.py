# python weight conversion
unit = input("Kilogram or pounds (K/L):")

weight = float(input("Entre your wight in the unit you provided us before:"))

if unit == "K":
    weight = weight * 2.205
    unit = 'lbs'
    print(f"your weight is:{round(weight)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "kg"
    print(f"your weight is:{round(weight)} {unit}")
else:
    print(f"UNKNOWN UNIT :{unit}")













