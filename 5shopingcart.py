item=input("Entre the name of the item?:")
price=float(input("Entre the price of the item?:"))
quantity=float(input("no of item you would like to buy?:"))


total_price= price*quantity
print(f"You have bought {str(quantity)} X {item}/s")
print(f"you total price would be ${round(total_price, 2)}")