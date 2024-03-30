keypad = ((1,2,3),
          (4,5,6),
          (7,8,9),
          ("*",0,"#"))

for numbers in keypad:
    for num in numbers:
        print(num,end=" | ")
    print()
