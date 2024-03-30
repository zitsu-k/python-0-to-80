# default argumentas = A default value for certain parameters 
#                      default is used when that argument is omitted
#                      make your functions more flexiable , reduce # of arguments 
#                      1. positional, 2.DEFAULT 3.kayword 4.arbitray:) 

# def net_price(list_price, discount= 00, tax = 0.05):
#     return list_price * (1-discount) *( 1+ tax)

# total_price = net_price(500,0.1,0)

# print("$",total_price)


import time



def count(end,start = 0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("done")

count(10)






