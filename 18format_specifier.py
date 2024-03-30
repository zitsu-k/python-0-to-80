# format specifiers = { value : flags} foramt a value based on what 
#                                       flags are inserted 
# .(number)f = round to that many dedimal places (fixed point)
# :(number) = allocate and zero pad that many spaces
# :< = left justify 
# :> = right justify
# :^ = centre allign 
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position 
# :  = insert a space before positive numbers
# :, = comma separator



price1 =232 
price2 = 234.434
price3 =2313.38

print(f"Price 1 is ${price1:.2f}")
print(f"Price 3 is ${price3:.2f}")
print(f"Price 2 is ${price2:.2f}")













