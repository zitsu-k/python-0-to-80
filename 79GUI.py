from tkinter import *

#widgets = GUI elements : buttons , textboxes , labels , images 
# windows - servies as a container to hold or contain these wedigets 
window = Tk() #instantate an in stance of a window 
window.geometry("420x420")
window.title("Zitsu k first GUI programe ")

icon  = PhotoImage(file='Screenshot (25).png')
window.iconphoto(True,icon)
window.config(background="green") # we can use hex color from google and write # befor the name so the programe can recoganize it as hex color

window.mainloop()# place window on computer screen ,listen  for events 
