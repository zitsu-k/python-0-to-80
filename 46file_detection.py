import os

path = "C:\\Users\\kaush\\OneDrive\\Desktop\\txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("that is a file ")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("that location dosn't exist")











