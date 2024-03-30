# python compound interest calculator

principal = 0
rate = 0 
time = 0 

while principal <= 0 :
    principal= float(input("Entre the principal amount :"))
    if principal <= 0 :
        print("principal can't be <= 0")

while rate <= 0 :
    rate = float(input("Entre the intrest rate amount :"))
    if rate <= 0 :
        print("intrest rate can't be <= 0")


while time <= 0 :
    time = float(input("Entre the time amount :"))
    if time <= 0 :
        print("time can't be <= 0")

total = principal*pow((1+ rate/100),time)
print(f"Balance after our variable {time} year/s : is ${total:.2f}.")

















































































































































