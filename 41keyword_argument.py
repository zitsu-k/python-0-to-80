# keyword arguments = an argument by and indentifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1.positional, 2. default , 3.KEYWORD , 4.arbitrary

# def hello(Greeting,title , first,last):
#     print(f"{Greeting},{title}{first} {last}")



# hello("Hello", title="MR.",first="spongbob",last="squarepants")


# for x in range(1,11):
    # print(x,end=" ")

# print("1","2","3","4",sep="-")

def get_phone (contry, area, first,last):
    return f"{contry}-{area}-{first}-{last}"

phone_num = get_phone(contry=1,area=234,first=23423,last=343)

print(phone_num)





















