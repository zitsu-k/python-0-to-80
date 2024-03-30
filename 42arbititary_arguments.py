# *args     = allows you to pass multipal non - key arguments 
# **kawargs = allows you to pass multiple keyword - arguments
#             * unpacking operator 
#             1. positional 2.default 3.keyword 4.ARBITRARY
  

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(2,3,5,12))



# def display_names(*args):
#     for arg in args:
#         print(arg,end = "")

# display_names("spongebob"," harold ","squarepants")



# def print_address(**kwargs):
#     for key ,value in kwargs.items():
#         print(f"{key}:{value}")

# print_address(street="123 fake st",
#               apt="100",
#               sity ="detroit",
#               state = "MI",
#               zip= "543221")






def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for value in kwargs.values():
        print(value,end = " ")
shipping_label("dr","zitsu","k",
               street = "chandwari",
               apt=23,
               city= "patna",
               state = "bihar",
               country = "INDIA")










