# Phyton credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left 
# 3. Double every second digit from right to left .
#      (If result is a two-digit number, add the two-digit number to get a single digit)
# 4. Sum the total of steps 2 & 3
# 5. If sum is divisible by 10 , the credit card  # is valid

sum_odd_digit = 0
sum_even_digit = 0
total =0

# Step 1 

card_number =input("Please Entre your credit card #: ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")

card_number= card_number[::-1]


# Step 2

for x in card_number[::2]:
    sum_odd_digit =sum_odd_digit + int(x)

print(sum_odd_digit)










































