#nested loops = A loop within another loop (ourter , inner) 
#               outer loop:
#                   inner loop:

for x in range(1,10):
    print(x,end="")

for x in range(3):
        for y in range(1,10):
            print(y,end=" ")
        print()



rows = int(input("Entre the no of rows?:"))

couloms = int(input("Entre the no of couloms?:"))

symbol = input("entre any symbol to use:")

for x in range(rows):
    for y in range(couloms):
        print(symbol,end="%")
    print()

































