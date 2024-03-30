
num1 = float(input("Entre the first no :"))

operator = input("Entre an operator(+ - * /):")

num2 = float(input("Entre the second no :"))

if operator == "/":
    print(num1/num2)
elif operator == "*":
    print(num1*num2)
elif operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
else:
    print(f"operation {operator} dosen't exist in the given operators")