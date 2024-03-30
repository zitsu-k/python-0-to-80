try:
    with open('D:\\work done\\text.txt') as file:    
        print(file.read())
except FileNotFoundError:
    print("File not found :(")

