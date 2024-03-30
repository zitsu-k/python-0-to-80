import os

source = "folder"
destination= "C:\\Users\\kaush\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source,destination)
        print(source+ " was moved")
except FileNotFoundError:
    print(source+" was not found")